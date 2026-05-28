def execute_workflow(email_data):

    category = email_data.get("category")
    priority = email_data.get("priority")

    print("\nWORKFLOW ACTIONS:\n")

    if priority == "high":
        print("🚨 High priority email detected")

    if category == "meeting":
        print("📅 Schedule meeting workflow triggered")

    elif category == "job":
        print("💼 Job-related workflow triggered")

    elif category == "finance":
        print("💰 Finance workflow triggered")

    elif category == "spam":
        print("🗑️ Spam filtering workflow triggered")

    else:
        print("📩 General workflow triggered")