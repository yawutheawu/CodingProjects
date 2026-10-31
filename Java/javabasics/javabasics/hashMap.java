package javabasics;

import java.util.HashMap;

import java.util.Map;

public class hashMap {

	public static void main(String[] args) {
		HashMap<String,String> testMap = new HashMap<>();
		
		testMap.put("Apple","Red");
		System.out.println(testMap.get("Apple"));
		System.out.println(testMap.containsKey("Apple"));
		
		//changeable inline hashmap
		Map<String, String> mutableMap = new HashMap<>(Map.of("Apple", "Red"));
		
		mutableMap.put("Apple", "Reddest");
		
		System.out.println("\n--- All Entries ---");
        for (Map.Entry<String, String> entry : mutableMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        //add remove
	}

}
