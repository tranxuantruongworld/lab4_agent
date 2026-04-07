import os
from agent import graph

def run_tests():
    test_cases = [
        # Test 1
        "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
        # Test 2
        "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng",
        # Test 3
        "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!",
        # Test 4
        "Tôi muốn đặt khách sạn",
        # Test 5
        "Giải giúp tôi bài tập lập trình Python về linked list",
        # Test 6
        "Tôi muốn đặt vé máy bay từ Đà Lạt đi Hải Phòng.",
        # Test 7
        "Tôi muốn đi Đà Nẵng, ở khách sạn Mường Thanh Luxury 2 đêm và bay Vietnam Airlines hạng Business. Tổng ngân sách tôi có là 3 triệu.",
        # Test 8
        "Tìm cho tôi khách sạn ở khu vực Mỹ Khê với giá dưới 1 triệu.",
        # Test 9
        "Tôi định đi từ Hà Nội vào HCM chơi 1 ngày, sau đó từ HCM bay ra Phú Quốc nghỉ dưỡng. Tổng ngân sách 10 triệu cho cả hành trình này."
    ]

    with open("test_results.md", "a", encoding="utf-8") as f:
        for i, test in enumerate(test_cases, 1):
            f.write(f"\n# Test {i}\n")
            f.write(f"**User**: {test}\n\n")
            
            # Use different thread_id for each test to keep contexts isolated in this test run
            config = {"configurable": {"thread_id": f"test_thread_{i}"}}
            
            print(f"Running Test {i}...")
            result = graph.invoke(
                {"messages": [("human", test)]},
                config=config
            )
            
            # Print intermediate steps (tool calls) if we want? The graph already has a print in agent_node, but it prints to stdout.
            # To capture it, we'd have to redirect stdout. Instead we can just inspect result["messages"]
            
            final = result["messages"][-1]
            f.write(f"**Agent**: {final.content}\n\n")
            
            # Let's see what tools were called
            tool_calls = []
            for msg in result["messages"]:
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    for tc in msg.tool_calls:
                        tool_calls.append(f"{tc['name']}({tc['args']})")
            
            if tool_calls:
                f.write("**Tools Called**:\n")
                for tc in tool_calls:
                    f.write(f"- `{tc}`\n")
                f.write("\n")

if __name__ == "__main__":
    run_tests()
