public class Direction {

    private final int _hours;

    private Direction(int hours) {
		
        hours = hours % 12;
        if (hours < 0) { hours += 12; }
		
        _hours = hours;
    }

	// branch 1
    public Direction anticlockwise() {
        return new Direction(this._hours - 3);
    }
	
	public static Direction north() {
        return new Direction(0);
    }
	
    public static Direction south() {
        return new Direction(6);
    }

	// branch 2
    public boolean isOpposite(Direction other) {
        return this.opposite().equals(other);
    }
	
    public static Direction east() {
        return new Direction(3);
    }

    public static Direction west() {
        return new Direction(9);
    }
}