
REJECTION_REASONS_MAP = {
    "fake_document": "Fake_document",
    "not_covered": "Not_Covered",
    "policy_expired": "Policy_expired"
}

def handle_error(message):
    print(f"[ERROR] {message}")
    return "Error"

def reason_in_text(text, keyword):
    try:
        if text and isinstance(text, str):
            return keyword.lower() in text.lower()
    except Exception as err:
        handle_error(f"Failed in reason_in_text: {str(err)}")
    return False

def identify_reason(text):
    try:
        for keyword, label in REJECTION_REASONS_MAP.items():
            if reason_in_text(text, keyword):
                return label
        return "Unknown"
    except Exception as err:
        return handle_error(f"identify_reason failed: {str(err)}")

def classify_rejection(text):
    try:
        if not isinstance(text, str) or not text.strip():
            return "Invalid Remark"

        if reason_in_text(text, "fake_document"):
            return "Fake_document"
        elif reason_in_text(text, "not_covered"):
            return "Not_Covered"
        elif reason_in_text(text, "policy_expired"):
            return "Policy_expired"
        else:
            return identify_reason(text)
    except Exception as err:
        return handle_error(f"classify_rejection failed: {str(err)}")
if __name__ == "__main__":
    sample_texts = [
        "Rejected due to fake_document detected",
        "Claim not covered under policy",
        "Policy_expired before claim date",
        "Remark with no known reason"
    ]

    for text in sample_texts:
        result = classify_rejection(text)
        print(f"Input: {text}\nClassified as: {result}\n")
