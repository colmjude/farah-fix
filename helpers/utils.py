def find_attribute_changes(original_obj, updated_obj):
    changes = []

    # Iterate over the attributes of the original object
    for attr_name in dir(original_obj):
        # Skip attributes that are not user-defined
        if not hasattr(original_obj, attr_name) or attr_name.startswith("__"):
            continue

        original_value = getattr(original_obj, attr_name, None)
        updated_value = getattr(updated_obj, attr_name, None)

        # Compare attribute values and record changes
        if original_value != updated_value:
            changes.append(f"Attribute '{attr_name}' changed: {original_value} -> {updated_value}")

    return changes
