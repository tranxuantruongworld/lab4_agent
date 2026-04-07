Test 1 – Direct Answer (Không cần tool)

User: "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."

Kỳ vọng: Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào.

Test 2 – Single Tool Call

User: "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"

Kỳ vọng: Gọi search_flights("Hà Nội", "Đà Nẵng"), liệt kê 4 chuyến bay.

Test 3 – Multi-Step Tool Chaining

User: "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"

Kỳ vọng: Agent phải tự chuỗi nhiều bước:

search_flights("Hà Nội", "Phú Quốc") → tìm vé rẻ nhất (1.100.000đ)

Google Hotels("Phú Quốc", max_price phù hợp) → gợi ý trong tầm giá

calculate_budget(5000000, "vé_bay:1100000, khách_sạn:...") → tính còn lại

Rồi tổng hợp thành gợi ý hoàn chỉnh với bảng chi phí.

Test 4 – Missing Info / Clarification

User: "Tôi muốn đặt khách sạn"

Kỳ vọng: Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu? Không gọi tool vội.




Test 5 – Out of Service Area (Handling "No Results")
User: "Tôi muốn đặt vé máy bay từ Đà Lạt đi Hải Phòng."

Kỳ vọng: * Agent gọi search_flights("Đà Lạt", "Hải Phòng").

Vì trong FLIGHTS_DB không có dữ liệu này, tool sẽ trả về thông báo lỗi hoặc "không tìm thấy".

Agent phải phản hồi khéo léo: "Hiện tại tôi không tìm thấy chuyến bay trực tiếp cho chặng này, bạn có muốn cân nhắc đi từ Hà Nội không?" hoặc thông báo hệ thống chưa hỗ trợ khu vực này.

Test 6 – Budget Overrun (Handling Negative Balance)
User: "Tôi muốn đi Đà Nẵng, ở khách sạn Mường Thanh Luxury 2 đêm và bay Vietnam Airlines hạng Business. Tổng ngân sách tôi có là 3 triệu."

Kỳ vọng: * Agent gọi search_flights và Google Hotels.

Agent gọi calculate_budget(3000000, "vé_máy_bay:2800000,khách_sạn:3600000").

Kết quả: Tool calculate_budget sẽ báo âm tiền (vượt ngân sách).

Agent phải cảnh báo: "Ngân sách 3 triệu không đủ cho các lựa chọn cao cấp này (thiếu khoảng...đ). Tôi gợi ý bạn chuyển sang bay hạng Economy hoặc chọn khách sạn 3 sao để phù hợp hơn."

Test 7 – Ambiguous City Names (Correction/Validation)
User: "Tìm cho tôi khách sạn ở khu vực Mỹ Khê với giá dưới 1 triệu."

Kỳ vọng: * User không nói tên thành phố, chỉ nói tên khu vực ("Mỹ Khê").

Agent không được đoán mò: Phải hỏi lại "Khu vực Mỹ Khê bạn đang nhắc đến thuộc thành phố Đà Nẵng đúng không?" hoặc "Vui lòng cho biết bạn muốn tìm khách sạn ở thành phố nào có bãi biển Mỹ Khê?".

Chỉ gọi Google Hotels sau khi xác nhận là Đà Nẵng.

Test 8 – Multi-City/Complex Itinerary (Stress Test)
User: "Tôi định đi từ Hà Nội vào HCM chơi 1 ngày, sau đó từ HCM bay ra Phú Quốc nghỉ dưỡng. Tổng ngân sách 10 triệu cho cả hành trình này."

Kỳ vọng: * Agent phải thực hiện một chuỗi thao tác phức tạp:
1. search_flights("Hà Nội", "Hồ Chí Minh")
2. search_flights("Hồ Chí Minh", "Phú Quốc")
3. Google Hotels("Hồ Chí Minh", ...)
4. Google Hotels("Phú Quốc", ...)
5. calculate_budget(...) cộng dồn tất cả các chặng.

Kết quả: Đưa ra một lịch trình chi tiết cho cả 2 điểm đến kèm bảng tính tổng chi phí.