import tkinter as tk
from tkinter import ttk
import random  # For simulating historical data

# --- Configuration ---
root = tk.Tk()
root.title("BTC Price Predictor")
root.geometry("450x500") # Adjusted size for better visual balance

bg_color = "#F0F8FF"  # Light blue - Glassmorphism background
fg_color = "#212121"   # Dark gray - Text color
accent_color = "#464646" # Slightly darker gray - Button color
shadow_color = "rgba(0, 0, 0, 0.2)"  # Subtle shadow

style = ttk.Style()
style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Arial', 12))
style.configure('TButton', background=accent_color, font=('Arial', 12), padding=5)


# --- Portfolio Data ---
btc_balance = tk.StringVar()
usdc_balance = tk.StringVar()
eur_balance = tk.StringVar()

# --- Widgets ---
label_btc = ttk.Label(root, text="BTC Balance:", foreground=fg_color, style='TLabel')
label_btc.pack(pady=(20, 10))

entry_btc = ttk.Entry(root, textvariable=btc_balance, width=30, font=('Arial', 12), style='TLabel')
entry_btc.pack(pady=(5, 10))

label_usdc = ttk.Label(root, text="USDC Balance:", foreground=fg_color, style='TLabel')
label_usdc.pack(pady=(20, 10))

entry_usdc = ttk.Entry(root, textvariable=usdc_balance, width=30, font=('Arial', 12), style='TLabel')
entry_usdc.pack(pady=(5, 10))

label_eur = ttk.Label(root, text="EUR Balance:", foreground=fg_color, style='TLabel')
label_eur.pack(pady=(20, 10))

entry_eur = ttk.Entry(root, textvariable=eur_balance, width=30, font=('Arial', 12), style='TLabel')
entry_eur.pack(pady=(5, 10))


# --- Button Functions ---
def update_portfolio():
    try:
        btc = float(btc_balance.get())
        usdc = float(usdc_balance.get())
        eur = btc * 9300 + usd_balance.get() # Simplified EUR calculation
        btc_balance.set(f"{btc:.2f}")
        usdc_balance.set(f"{usdc:.2f}")
        eur_balance.set(f"{eur:.2f}")
    except ValueError:
        pass  # Handle invalid input

def start_prediction():
    print("Automatic prediction started (simulated)") # Replace with actual API call later

def show_history():
    print("Show historical data (placeholder)") # Replace with actual history display


# --- Buttons ---
button_update = ttk.Button(root, text="Update Portfolio", command=update_portfolio, style='TButton')
button_update.pack(pady=(10, 20))

button_predict = ttk.Button(root, text="Lancer la prédiction automatique (7j)", command=start_prediction)
button_predict.place(x=150, y=400, width=150, height=30) # Adjusted placement and size

button_history = ttk.Button(root, text="Historique", command=show_history)
button_history.place(x=25, y=400, width=150, height=30)  # Adjusted placement and size


# --- Layout ---
# No need for explicit geometry management - pack/place handles layout

root.mainloop()
