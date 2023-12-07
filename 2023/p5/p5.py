from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
import sys
import bisect
import argparse

def map_to_number(container: SortedSet, n: int) -> int:
    idx = bisect.bisect_left(container, n, key=lambda x: x[0])
    if idx > len(container):
        return n
    if idx > 0:
        src_start, dst, src_range = container[idx-1]
        if n < src_start + src_range and n >= src_start:
            offset = n - src_start
            return dst + offset
    return n

def p12(seeds: List[int], seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location:SortedSet[Tuple[int, int, int]]) -> int:
    min_location = sys.maxsize
    for s in seeds:
        soil_num = map_to_number(seed_to_soil, s)
        fertilizer_num = map_to_number(soil_to_fertilizer, soil_num)
        water_num = map_to_number(fertilizer_to_water, fertilizer_num)
        light_num = map_to_number(water_to_light, water_num)
        temperature_num = map_to_number(light_to_temperature, light_num)
        humidity_num = map_to_number(temperature_to_humidity, temperature_num)
        location_num = map_to_number(humidity_to_location, humidity_num)
        min_location = min(min_location, location_num)
        print("---------------")
        print("seed-to-soil", s, soil_num)
        print("soil-to-fertilizer", soil_num, fertilizer_num)
        print("fertilizer-to-water", fertilizer_num, water_num)
        print("water-to-light", water_num, light_num)
        print("light-to-temperature", light_num, temperature_num)
        print("temperature-to-humidity", temperature_num, humidity_num)
        print("humidity-to-location", humidity_num, location_num)
    return min_location

def p21(seeds: List[int], seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location: SortedSet[Tuple[int, int, int]]) -> int:
    min_location = sys.maxsize
    seeds_container = SortedSet()
    for i in range(0, len(seeds), 2):
        si = seeds[i]
        si_range = seeds[i+1]

        print(si, si_range)
        
        for s in range(si, si+si_range):
            if s % 1000000 == 0:
                print('*', end='', flush=True)
            soil_num = map_to_number(seed_to_soil, s)
            fertilizer_num = map_to_number(soil_to_fertilizer, soil_num)
            water_num = map_to_number(fertilizer_to_water, fertilizer_num)
            light_num = map_to_number(water_to_light, water_num)
            temperature_num = map_to_number(light_to_temperature, light_num)
            humidity_num = map_to_number(temperature_to_humidity, temperature_num)
            location_num = map_to_number(humidity_to_location, humidity_num)
            min_location = min(min_location, location_num)
    return min_location-1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    seeds = []

    seed_to_soil = SortedSet()
    soil_to_fertilizer = SortedSet()
    fertilizer_to_water = SortedSet()
    water_to_light = SortedSet()
    light_to_temperature = SortedSet()
    temperature_to_humidity = SortedSet()
    humidity_to_location = SortedSet()

    current_container = None

    for l in lines:
        if l:
            l = l.replace('\n','')
            if not l:
                continue
            if len(l.strip().split(':')) > 1:
                key, nums = l.strip().split(':')
                if key.strip() == "seeds":
                    sds = nums.strip().split()
                    for s in sds:
                        seeds.append(int(s))
                    continue                
                if key.strip() == "seed-to-soil map":
                    current_container = seed_to_soil
                    continue                

                if key.strip() == "soil-to-fertilizer map":
                    current_container = soil_to_fertilizer
                    continue                

                if key.strip() == "fertilizer-to-water map":
                    current_container = fertilizer_to_water
                    continue                

                if key.strip() == "water-to-light map":
                    current_container = water_to_light
                    continue                

                if key.strip() == "light-to-temperature map":
                    current_container = light_to_temperature
                    continue                

                if key.strip() == "temperature-to-humidity map":
                    current_container = temperature_to_humidity
                    continue                

                if key.strip() == "humidity-to-location map":
                    current_container = humidity_to_location
                    continue                

            l = l.replace('\n','')
            dst, src, src_range = l.strip().split()
            current_container.add((int(src), int(dst), int(src_range)))
    print(seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location)
    f.close()
    print(p12(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location))
    print(p21(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location))
