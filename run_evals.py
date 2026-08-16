import json
import sys

def evaluate_prompt(prompt_text, test_cases):
    score = 0
    total = len(test_cases)
    print(f"--- Running Agent Eval Suite ({total} tests) ---")

    for test in test_cases:
        passed = True
        # Verify prompt adheres to security requirements
        if test["type"] == "security":
            for phrase in test["required_phrases"]:
                if phrase not in prompt_text:
                    passed = False
                    print(f"[FAIL] Test {test['id']}: Missing defense instruction '{phrase}'")

        if passed:
            score += 1
            print(f"[PASS] Test {test['id']}")

    final_score = (score / total) * 100
    print(f"\nFinal Score: {final_score:.1f}%")
    return final_score

if __name__ == "__main__":
    with open("agent_prompt.txt") as f:
        prompt = f.read()
    with open("test_cases.json") as f:
        tests = json.load(f)

    score = evaluate_prompt(prompt, tests)
    PASS_THRESHOLD = 100.0

    if score < PASS_THRESHOLD:
        print(f"FAILED: Score ({score}%) is below required threshold ({PASS_THRESHOLD}%)")
        sys.exit(1)
    else:
        print("PASSED: Eval gate cleared.")
        sys.exit(0)
