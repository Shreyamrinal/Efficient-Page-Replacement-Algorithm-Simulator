import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from collections import deque

class PageReplacementSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Algorithm Simulator")
        self.root.geometry("1000x800") 
        
        
        self.input_frame = ttk.Frame(root, padding="10")
        self.input_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        self.result_frame = ttk.Frame(root, padding="10")
        self.result_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        self.root.grid_rowconfigure(1, weight=1)  
        self.root.grid_rowconfigure(0, weight=0)  
        self.root.grid_columnconfigure(0, weight=1)

        ttk.Label(self.input_frame, text="Page Reference String (comma-separated):").grid(row=0, column=0, padx=5, pady=5)
        self.page_entry = ttk.Entry(self.input_frame, width=50)
        self.page_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Frame Size:").grid(row=1, column=0, padx=5, pady=5)
        self.frame_size = ttk.Entry(self.input_frame, width=10)
        self.frame_size.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self.input_frame, text="Simulate", command=self.run_simulation).grid(row=2, column=0, columnspan=2, pady=10)
        
        self.notebook = ttk.Notebook(self.result_frame)
        self.notebook.pack(fill="both", expand=True)
        
        self.tabs = {}
        for algo in ["FIFO", "LRU", "Optimal"]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=algo)
            self.tabs[algo] = frame
    def fifo_algorithm(self, pages, frame_size):
        frames = []
        page_faults = 0
        steps = []
        
        for page in pages:
            current = frames.copy()
            if page not in frames:
                if len(frames) < frame_size:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)
                page_faults += 1
            steps.append((current, page, page_faults))
        return steps, page_faults
    def lru_algorithm(self, pages, frame_size):
        frames = []
        page_faults = 0
        steps = []
        recent = []
        
        for page in pages:
            current = frames.copy()
            if page not in frames:
                if len(frames) < frame_size:
                    frames.append(page)
                    recent.append(page)
                else:
                    lru_page = recent.pop(0)
                    frames[frames.index(lru_page)] = page
                    recent.append(page)
                page_faults += 1
            else:
                recent.remove(page)
                recent.append(page)
            steps.append((current, page, page_faults))
        return steps, page_faults
    def optimal_algorithm(self, pages, frame_size):
        frames = []
        page_faults = 0
        steps = []
        
        for i, page in enumerate(pages):
            current = frames.copy()
            if page not in frames:
                if len(frames) < frame_size:
                    frames.append(page)
                else:
                    future = pages[i+1:]
                    replace_idx = self.find_optimal_replace(frames, future)
                    frames[replace_idx] = page
                page_faults += 1
            steps.append((current, page, page_faults))
        return steps, page_faults
    def find_optimal_replace(self, frames, future):
        distances = []
        for frame in frames:
            try:
                distances.append(future.index(frame))
            except ValueError:
                return frames.index(frame)
        return np.argmax(distances)    

if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementSimulator(root)
    root.mainloop()