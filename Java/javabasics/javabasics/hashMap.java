package javabasics;

import java.util.HashMap;

import java.util.Map;

public class hashMap {

	public static void main(String[] args) {
		HashMap<String,String> testMap = new HashMap<>();
		
		testMap.put("Apple","Red");
		// {"Apple":"Red"}
		System.out.println(testMap.get("Apple"));
		System.out.println(testMap.containsKey("Apple"));
		
		//changeable inline hashmap (Up to 10)
		Map<String, String> mutableMap = new HashMap<>(Map.of("Apple", "Red","Orange","Orange"));
		
		//unchangeable inline map (no limit)
		Map<String, Integer> map = Map.ofEntries(
			    Map.entry("One", 1),
			    Map.entry("Two", 2),
			    Map.entry("Three", 3)
			);
		
		//changeable inline hashmap (No Limit)
		Map<String, String> mutableMapLong = new HashMap<>(Map.ofEntries(
				Map.entry("Apple", "Green"),
				Map.entry("Orange", "Orange"),
				Map.entry("Banana", "Yellow"),
				Map.entry("Dragonfruit", "Red-Yellow"),
				Map.entry("Jackfruit", "Brown"),
				Map.entry("Coconut", "Brown"),
				Map.entry("Avocado", "Dark Green"),
				Map.entry("Mango", "Yellow-Red"),
				Map.entry("Cherry", "Dark Red"),
				Map.entry("Strawberry", "Red"),
				Map.entry("Blueberry", "Blue")
			));
		
		mutableMap.put("Apple", "Reddest");
		
//		System.out.println("\n--- All Entries ---");
//		//dict.items() -> [[key,value]...]
//        for (Map.Entry<String, String> entry : mutableMap.entrySet()) {
//            System.out.println(entry.getKey() + ": " + entry.getValue());
//        }
        
        System.out.println("\n--- All Entries Long ---");
        // .entrySet() -> key value pair array .keySet() -> Key Array .values() -> value array
        for (Map.Entry<String, String> entry : mutableMapLong.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("\n");
        System.out.println(mutableMapLong.size());
        //remove key/val from hashmap
        mutableMapLong.remove("Orange");
        
        System.out.println("\n--- All Entries Long ---");
        for (Map.Entry<String, String> entry : mutableMapLong.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("\n");
        System.out.println(mutableMapLong.size());
        //clear HashMap
        mutableMapLong.clear();
        
        System.out.println("\n--- All Entries Long ---");
        for (Map.Entry<String, String> entry : mutableMapLong.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("\n");
        System.out.println(mutableMapLong.size());
	}

}
