
# Test 1
**User**: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

**Agent**: Chào bạn! Thật tuyệt khi bạn đang có kế hoạch đi du lịch. Bạn có ý tưởng nào về điểm đến chưa? Hoặc bạn muốn tôi gợi ý một số địa điểm nổi tiếng ở Việt Nam như Đà Nẵng, Phú Quốc, hay Hà Nội? Hãy cho tôi biết nhé!


# Test 2
**User**: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

**Agent**: Dưới đây là danh sách chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines (economy)**: 06:00 -> 07:20 | Giá: 1.450.000đ
2. **Vietnam Airlines (business)**: 14:00 -> 15:20 | Giá: 2.800.000đ
3. **VietJet Air (economy)**: 08:30 -> 09:50 | Giá: 890.000đ
4. **Bamboo Airways (economy)**: 11:00 -> 12:20 | Giá: 1.200.000đ

Bạn có muốn tôi tìm khách sạn ở Đà Nẵng không? Nếu có, hãy cho tôi biết ngân sách tối đa mỗi đêm của bạn nhé!

**Tools Called**:
- `search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})`


# Test 3
**User**: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

**Agent**: Dưới đây là thông tin chuyến đi của bạn từ Hà Nội đến Phú Quốc trong 2 đêm:

**Chuyến bay:**
- **VietJet Air (economy)**: 10:00 -> 12:15 | Giá: **1.350.000đ**

**Khách sạn:**
- **Sol by Meliá (4 sao)** - 4.2⭐ | Khu vực: Bãi Trường | Giá: **1.500.000đ/đêm** (Tổng cho 2 đêm: **3.000.000đ**)
- Hoặc bạn có thể chọn **9Station Hostel (2 sao)** - 4.5⭐ | Khu vực: Dương Đông | Giá: **200.000đ/đêm** (Tổng cho 2 đêm: **400.000đ**)

**Tổng chi phí ước tính:**
- Nếu chọn Sol by Meliá: **4.350.000đ** (1.350.000đ vé máy bay + 3.000.000đ khách sạn)
- Nếu chọn 9Station Hostel: **1.750.000đ** (1.350.000đ vé máy bay + 400.000đ khách sạn)

**Ngân sách còn lại:**
- Nếu chọn Sol by Meliá: **650.000đ**
- Nếu chọn 9Station Hostel: **3.250.000đ**

**Gợi ý thêm:**
- Nếu bạn muốn tiết kiệm, 9Station Hostel là lựa chọn tuyệt vời với giá cả phải chăng.
- Nếu bạn muốn trải nghiệm sang trọng hơn, Sol by Meliá sẽ mang lại cho bạn một kỳ nghỉ thoải mái.

Bạn có muốn đặt vé máy bay và khách sạn không?

**Tools Called**:
- `search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})`
- `search_hotels({'city': 'Phú Quốc'})`
- `calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1350000,khách_sạn:1600000'})`


# Test 4
**User**: Tôi muốn đặt khách sạn

**Agent**: Bạn muốn đặt khách sạn ở thành phố nào? Và bạn có ngân sách tối đa cho mỗi đêm là bao nhiêu không?


# Test 5
**User**: Giải giúp tôi bài tập lập trình Python về linked list

**Agent**: Xin lỗi, nhưng mình chỉ hỗ trợ các thông tin liên quan đến du lịch. Nếu bạn có câu hỏi nào về chuyến đi, điểm đến hay kế hoạch du lịch, hãy cho mình biết nhé!


# Test 6
**User**: Tôi muốn đặt vé máy bay từ Đà Lạt đi Hải Phòng.

**Agent**: Hiện tại, mình chưa có thông tin về chuyến bay từ Đà Lạt đi Hải Phòng. Bạn có muốn tìm chuyến bay từ Đà Lạt đến một thành phố khác không? Hoặc bạn có thể cung cấp thêm thông tin về chuyến đi của mình?


# Test 7
**User**: Tôi muốn đi Đà Nẵng, ở khách sạn Mường Thanh Luxury 2 đêm và bay Vietnam Airlines hạng Business. Tổng ngân sách tôi có là 3 triệu.

**Agent**: Trước tiên, mình sẽ tìm chuyến bay Vietnam Airlines hạng Business từ thành phố của bạn đến Đà Nẵng. Bạn có thể cho mình biết bạn khởi hành từ thành phố nào không?


# Test 8
**User**: Tìm cho tôi khách sạn ở khu vực Mỹ Khê với giá dưới 1 triệu.

**Agent**: Khu vực Mỹ Khê bạn đang nhắc đến thuộc thành phố Đà Nẵng đúng không?


# Test 9
**User**: Tôi định đi từ Hà Nội vào HCM chơi 1 ngày, sau đó từ HCM bay ra Phú Quốc nghỉ dưỡng. Tổng ngân sách 10 triệu cho cả hành trình này.

**Agent**: Mình đã tìm thấy các chuyến bay cho hành trình của bạn như sau:

### Chuyến bay từ Hà Nội đến Hồ Chí Minh:
1. **Vietnam Airlines (economy)**: 06:00 -> 08:10 | Giá: **1.600.000đ**
2. **VietJet Air (economy)**: 07:30 -> 09:40 | Giá: **950.000đ**
3. **Bamboo Airways (economy)**: 12:00 -> 14:10 | Giá: **1.300.000đ**
4. **Vietnam Airlines (business)**: 18:00 -> 20:10 | Giá: **3.200.000đ**

### Chuyến bay từ Hồ Chí Minh đến Phú Quốc:
1. **Vietnam Airlines (economy)**: 08:00 -> 09:00 | Giá: **1.100.000đ**
2. **VietJet Air (economy)**: 15:00 -> 16:00 | Giá: **650.000đ**

Tiếp theo, mình sẽ tìm khách sạn ở Phú Quốc. Bạn có ngân sách tối đa cho mỗi đêm ở khách sạn không?

**Tools Called**:
- `search_flights({'origin': 'Hà Nội', 'destination': 'Hồ Chí Minh'})`
- `search_flights({'origin': 'Hồ Chí Minh', 'destination': 'Phú Quốc'})`

