import json 
import asyncio

LOCAL_DB = "database.json"

async def main():
    while True:
        keyword = input("Search: ")
        
        with open(LOCAL_DB, "r") as f:
            load_db = json.load(f)
        
        filtered_data = {}
        for file_type in load_db:
            collection = load_db.get(file_type)
            for region in collection:
                region_data_coll = collection.get(region)

                for game_id in region_data_coll:
                    game_data = region_data_coll.get(game_id)
                    game_name = game_data.get("name")
                    if keyword.lower() in game_name.lower():
                        check_exist = filtered_data.get(file_type)
                        if check_exist:
                            check_exist.update({game_id: game_data})
                        else:
                            filtered_data.update({file_type: {game_id: game_data}})
            
        with open("output.json", "w") as f:
            json.dump(filtered_data, f, indent=4)
        
        if filtered_data == {}:
            print(f"{keyword} not found...")
        else:
            print("Check output.json")


asyncio.run(main())