import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np

    #O(nxm) complexity
    def generate_map(n=5, m=5, tree_prob=.6, fire_prob=.05, station_prob=.02, wall_prob=0.1):
        #generate firemap with zeros as default value
        firemap = np.zeros((n, m), dtype=int)

        #Init positions for fire and station
        fire_positions = set()
        station_positions = set()
        
        #encode values for each type.
        # 1 = tree
        # 2 = fire
        # 3 = fire station
        # 4 = wall
        firemap[np.random.rand(n,m) < tree_prob] = 1
        firemap[np.random.rand(n,m) < fire_prob] = 2
        firemap[np.random.rand(n,m) < station_prob] = 3
        firemap[np.random.rand(n,m) < wall_prob] = 4

        #Remove all fire from non tree probability locations
        firemap[(firemap == 2) & (np.random.rand(n,m) > tree_prob)] = 0

        fire_positions = {(r,c) for r, c in zip(*np.where(firemap == 2))}
        station_positions = {(r,c) for r, c in zip(*np.where(firemap == 3))}

        print(f"fire count = {len(fire_positions)}\n station count ={len(station_positions)}")
        
        #Return firemap, position of fires and fire stations
        return firemap, fire_positions, station_positions


    grid, fire_set, station_set = generate_map(n=30, m=30)
    return fire_set, generate_map, grid, np, station_set


app._unparsable_cell(
    r"""
    #for fires / stations, look for adjacent trees/empty space
    def get_adjacent(grid, row, col, type):
        neighbor_offsets = [(-1, 0), (1, 0), (0 -1), (0, 1)]

        ret = set()

        rows, cols = grid.shape

        for r_mod, c_mod in neighbor_offsets:
            nr, nc = row + r_mod, col + c_mod

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == type:
                #If searching for trees, set it on fire
                if type == 1:
                    grid[(nr,nc)] = 2
                elif type == 0:
                    #set first found blank space to firefighter
                    grid[(nr,nc)] = 5
                    return
            

    def fire_tick(grid, fire_pos):
        for (r,c) in fire_pos:
            tree_neighbors = get_adjacent(grid, r, c, 1)
            

    def station_tick(grid, station_pos, firefighters):
        if len(firefighters == 0):
            for (r,c) in station_pos:
                blank_neighbors
        else:

    def simulate(grid, fire_pos, station_pos):
        ticks = 0
        firefighters = set()
        while len(fire_pos) > 0:
            fire_tick(grid, fire_pos)
            
            station_pos(grid, station_pos, firefighters)
            ticks++
            
        print(f\"Fires extinguished in {ticks} ticks\")

    simulate(grid, fire_set, station_set)
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
