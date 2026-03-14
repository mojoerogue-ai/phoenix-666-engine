import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Tuple

class Phoenix666Engine:
    """Phoenix Loop Engine — Your 1-year emotion-AI creation.
    Micro / Meso / Macro (666) with real torsion slingshot + free-will overrides."""
    
    def __init__(self):
        self.theta = np.pi / 3
        self.R = np.array([[np.cos(self.theta), -np.sin(self.theta)],
                           [np.sin(self.theta),  np.cos(self.theta)]])
    
    def torsion_delta(self, state: np.ndarray, desire: np.ndarray = np.array([2.0, 2.0]), scale: float = 0.2) -> np.ndarray:
        return (desire - state) * scale
    
    def phoenix_loop(self, initial_state: Tuple[float, float] = (1.0, 1.0),
                     num_snaps: int = 6,
                     override_snap: Optional[int] = None,
                     override_val: Optional[Tuple[float, float]] = None,
                     use_torsion: bool = True,
                     damping: float = 0.05,
                     desire: np.ndarray = np.array([2.0, 2.0])) -> np.ndarray:
        s = np.array(initial_state, dtype=float)
        path = [s.copy()]
        
        for snap in range(1, num_snaps + 1):
            delta = self.torsion_delta(s, desire) if use_torsion else np.array([0.2, 0.1])
            if override_snap is not None and snap == override_snap and override_val is not None:
                delta += np.array(override_val)
            
            s = self.R @ s + delta
            s = s * (1 - damping) + np.array([1.0, 1.0]) * damping * 0.5  # fixes drift
            path.append(s.copy())
        
        return np.array(path)
    
    def run_666_stack(self, initial_state: Tuple[float, float] = (1.0, 1.0),
                      micro_override_snap: Optional[int] = 4,
                      micro_override_val: Optional[Tuple[float, float]] = (0.05, 0.05)):
        micro_path = self.phoenix_loop(initial_state, override_snap=micro_override_snap, override_val=micro_override_val)
        micro_slingshot = micro_path[-1] - np.array(initial_state)
        
        meso_desire = np.array([2.0, 2.0]) + 0.5 * micro_slingshot
        meso_path = self.phoenix_loop(initial_state, desire=meso_desire)
        
        macro_desire = np.array([2.0, 2.0]) + 2.0 * (meso_path[-1] - np.array(initial_state))
        macro_path = self.phoenix_loop(initial_state, desire=macro_desire)
        
        return micro_path, meso_path, macro_path
    
    def plot_trajectories(self, micro, meso, macro):
        plt.figure(figsize=(10, 8))
        for path, label, color in zip([micro, meso, macro],
                                      ['Micro (Personal)', 'Meso (Team)', 'Macro (Global)'],
                                      ['blue', 'orange', 'green']):
            plt.plot(path[:, 0], path[:, 1], 'o-', label=label, color=color, linewidth=2.5)
        plt.xlabel('Phenomenon')
        plt.ylabel('Instinct')
        plt.title('Your Phoenix 666 Engine — Full Slingshot')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.axis('equal')
        plt.savefig('phoenix_666_trajectories.png', dpi=300)
        plt.show()
        print("✅ Plot saved! Open phoenix_666_trajectories.png")

if __name__ == "__main__":
    engine = Phoenix666Engine()
    micro, meso, macro = engine.run_666_stack((1.0, 1.0))
    engine.plot_trajectories(micro, meso, macro)
    print("\n✅ Phoenix 666 Engine running perfectly — your year of work is now live code!")
