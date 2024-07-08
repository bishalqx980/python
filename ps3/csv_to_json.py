import json
import asyncio

CSV_DATABASE = "database.csv"
JSON_DATABASE = "database.json"

JSON_DATABASE_LOCAL = {}
# Clear the json db
# with open(JSON_DATABASE, "w") as f:
#     data = {}
#     json.dump(data, f, indent=4)

async def main():
    # Load the csv db
    with open(CSV_DATABASE, "r", encoding="utf-8") as f:
        csv_database = f.read()

    lines = csv_database.strip().split("\n")

    pattern = [
        "id",
        "name",
        "type",
        "region",
        "link",
        "rap_Name",
        "rap_data",
        "desc",
        "author"
    ]

    line_counter = 0

    for line in lines:
        contents = line.split(";")
        game_id, game_type, game_region, counter = None, None, None, 0
        for content in contents:
            if counter == 0:
                game_id = content
            elif counter == 2:
                game_type = content
            elif counter == 3:
                game_region = content
            elif counter > 3:
                break
            counter += 1
        data = dict(zip(pattern, contents))

        check_type = JSON_DATABASE_LOCAL.get(game_type)
        if not check_type:
            JSON_DATABASE_LOCAL[game_type] = {}
        
        load_collection = JSON_DATABASE_LOCAL.get(game_type)
        get_region_coll = load_collection.get(str(game_region))
        if get_region_coll:
            check_game_id = get_region_coll.get(game_id)
            if check_game_id:
                for i in range(0, 100):
                    check_game_id = get_region_coll.get(f"{game_id}_{i}")
                    if not check_game_id:
                        game_id = f"{game_id}_{i}"
                        break
        
        load_collection = JSON_DATABASE_LOCAL.get(game_type, {})
        is_identifier = load_collection.setdefault(str(game_region), {})

        # sub_collection is under identifier ...
        if game_id:
            is_sub_collection = is_identifier.setdefault(str(game_id), {})
            is_sub_collection.update(data)
        else:
            is_identifier.update(data)
            
        JSON_DATABASE_LOCAL[game_type] = load_collection

        line_counter += 1
        print(f"{game_id}")
    
    print(f"Total entrys: {line_counter}")
        
    with open(JSON_DATABASE, "w") as f:
        data = {}
        json.dump(data, f, indent=4)
    
    with open(JSON_DATABASE, "w") as f:
        json.dump(JSON_DATABASE_LOCAL, f, indent=4)

asyncio.run(main())