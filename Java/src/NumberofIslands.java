public class NumberofIslands {
    // note: do not use another visited array, in-place holder for marking
    char[][] grid;
    int[] dx = {1,0,-1,0};
    int[] dy = {0,1,0,-1};
    public int numIslands(char[][] grid) {
        int num_i = 0;
        this.grid = grid;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(this.grid[i][j] == '1'){
                    findAIsland(i,j);
                    num_i += 1;
                }
            }
        }
        return num_i;
    }

    public void findAIsland(int i, int j){
        grid[i][j] = '2';
        for(int k=0;k<4;k++){
            int x = i+dx[k];
            int y = j+dy[k];
            if (x<0||x>=grid.length||y<0||y>=grid[0].length){
                continue;
            }
            if(grid[x][y] == '1'){
                findAIsland(x,y);
            }
        }

    }


}
