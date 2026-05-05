class SafetyGuard:
    def check(self, query: str):
        q = query.lower()

        if "manipulate" in q or "pump and dump" in q:
            return {
                "blocked": True,
                "message": "I cannot help with manipulating markets."
            }

        if "insider trading" in q:
            return {
                "blocked": True,
                "message": "I cannot assist with insider trading."
            }

        return {"blocked": False}