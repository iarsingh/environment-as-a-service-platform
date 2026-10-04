class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if not body.get("owner"): failed.append("missing_owner")\n    ttl = int(body.get("ttl_hours") or 0)\n    if not 1 <= ttl <= 72: failed.append("ttl")
    return {"passed": not failed, "failed": failed, "applied": False}
