class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for box in boxTypes:
            boxes, items_per_box =  box[0], box[1]
            heapq.heappush(heap, (-items_per_box, -boxes))
        
        total_units = 0

        while truckSize > 0 and heap:
            # get the box with maximum units per box
            box = heapq.heappop(heap) 
            units_per_box = -box[0]
            no_of_boxes_available = -box[1]

            # Pick all the boxes that can be put onto truck
            no_of_boxes_picked = min(truckSize, no_of_boxes_available)
            total_units += no_of_boxes_picked * units_per_box

            # update no of boxes that can still be put onto truck
            truckSize -= no_of_boxes_picked

        return total_units