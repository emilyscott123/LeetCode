
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.seen = [False] * len(rooms) 

        def visit_rooms(room):
            self.seen[room] = True 

            for next_room in rooms[room]:
                if not self.seen[next_room]:
                    visit_rooms(next_room) 
            
        visit_rooms(0) 
        return sum(self.seen) == len(rooms)