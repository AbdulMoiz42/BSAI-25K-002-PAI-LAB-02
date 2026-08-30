SYSTEM_CONFIG = (
    "EnterprisePortal",
    "2.4.1",
    frozenset(["Development", "Staging", "Production"]),
    ("localhost", 5432, "admin_user")
)

print(f"Starting {SYSTEM_CONFIG[0]} v{SYSTEM_CONFIG[1]}...")
print(f"Connecting to database at {SYSTEM_CONFIG[3][0]}:{SYSTEM_CONFIG[3][1]}...\n")

print("[System Test] Attempting to modify configuration...")

SYSTEM_CONFIG[0] = "HackedApplication"

print("This line will never be printed.")
