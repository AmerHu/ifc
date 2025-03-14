import ifcopenshell

def analyze_ifc_rooms(file_path):
    try:
        ifc_file = ifcopenshell.open(file_path)
        print(f"file loaded : {file_path}")
        rooms = ifc_file.by_type("IfcSpace")
        print(f"\n  find  {len(rooms)} room :\n" + "="*40)

        for room in rooms:
            name = room.Name if room.Name else "no name"
            print(f"room : {name}")

            if hasattr(room, "ObjectType") and room.ObjectType:
                print(f"  - Object: {room.ObjectType}")
            if hasattr(room, "Description") and room.Description:
                print(f"  - Description: {room.Description}")

            print("  - Properties :")
            for rel in room.IsDefinedBy:
                if rel.is_a("IfcRelDefinesByProperties"):
                    prop_set = rel.RelatingPropertyDefinition
                    if prop_set.is_a("IfcPropertySet"):
                        for prop in prop_set.HasProperties:
                            value = prop.NominalValue.wrappedValue if prop.NominalValue else "N/A"
                            print(f"    • {prop.Name}: {value}")

            print("-"*40)

    except Exception as e:
        print(f"error in  : {str(e)}")

file_path = "Project.ifc"
analyze_ifc_rooms(file_path)