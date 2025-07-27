import tkinter as tk
import random
import os
import sys

#---------- Creating the window ----------#
root = tk.Tk()
root.title("NumberGuesser")

#---------- Dynamic icon path ----------#
def get_resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

# USE FORWARD SLASHES OR os.path.join - this is the fix!
icon_path = get_resource_path(os.path.join("icons", "icon_256.ico"))

# Add error handling for the icon
try:
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f"Icon not found at: {icon_path}")
except tk.TclError as e:
    print(f"Could not load icon: {e}")
    # Program continues without icon

root.geometry("250x100")
root.resizable(False, False)

#---------- Centering the window ----------#

root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#---------- Outer frame ----------#
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

#---------- Inner frame ----------#
inner_frame = tk.Frame(frame)
inner_frame.place(relx=0.5, rely=0.5, anchor='center')

#---------- Text label ----------#
label = tk.Label(inner_frame, text="Type the number you are thinking of below:")
label.pack(pady=10)

#---------- Entry + Button in same frame ----------#
input_frame = tk.Frame(inner_frame)
input_frame.pack()

#---------- Validation: max 18 digits ----------#
def is_valid(text):
    if text.isdigit() and len(text) <= 18:
        button.config(state='normal')
        return True
    else:
        button.config(state='disabled')
        return text == ""

vcmd = root.register(is_valid)

#---------- Entry box ----------#
entry = tk.Entry(input_frame, justify='center', validate="key", validatecommand=(vcmd, "%P"))
entry.pack(side='left', padx=5)

#---------- Button (initially disabled) ----------#
button = tk.Button(input_frame, text="Guess My Number", state='disabled')
button.pack(side='left', padx=5)

#---------- Result label ----------#
result_label = tk.Label(inner_frame, text="")
result_label.pack(pady=10)

#---------- Button behavior ----------#
def guess_number():
    number = entry.get()
    button.config(state='disabled')  # Disable during loading

    messages = [
        ("Analyzing brainwaves...", (0, 200)),
        ("Calibrating neural scanner...", (500, 700)),
        ("Synchronizing thought patterns...", (500, 700)),
        ("Decoding subconscious signals...", (500, 700)),
        ("Cross-referencing your memories...", (10, 100)),
        ("Retrieving neural data from deep storage...", (500, 700)),
        ("Consulting your inner oracle...", (10, 100)),
        ("Translating cryptic thoughts...", (10, 100)),
        ("Harmonizing cerebral frequencies...", (500, 700)),
        ("Scraping your imagination archive...", (500, 700)),
        ("Pinged your left brain... waiting for response...", (10, 100)),
        ("Unwrapping encrypted daydreams...", (500, 700)),
        ("Gathering psychic dust particles...", (10, 100)),
        ("Mind tether successfully established...", (10, 100)),
        ("Surveying your mental terrain...", (10, 100)),
        ("Scanning emotion pixels...", (10, 100)),
        ("Validating internal monologue patterns...", (10, 100)),
        ("Syncing with your telepathic pulse...", (10, 100)),
        ("Listening to your future thoughts...", (10, 100)),
        ("Buffering abstract logic...", (10, 100)),
        ("Decrypting daydream metadata...", (500, 700)),
        ("Performing sanity checksum...", (10, 100)),
        ("Teleporting your thought to hyperspace...", (10, 100)),
        ("Establishing cranial uplink...", (10, 100)),
        ("Running reality distortion algorithm...", (10, 100)),
        ("Compressing cognitive fragments...", (10, 100)),
        ("Exchanging mental metadata...", (10, 100)),
        ("Booting quantum intuition engine...", (10, 100)),
        ("Sifting through cerebral archives...", (10, 100)),
        ("Aligning memory lattice...", (10, 100)),
        ("Capturing stray neuron activity...", (10, 100)),
        ("Calibrating consciousness tracker...", (10, 100)),
        ("Tracking daydream emissions...", (10, 100)),
        ("Digitizing imagination bursts...", (10, 100)),
        ("Engaging emotional amplifier...", (500, 700)),
        ("Indexing hypothetical scenarios...", (500, 700)),
        ("Probing metaphor generators...", (10, 100)),
        ("Filtering logic vs. impulse matrix...", (10, 100)),
        ("Reading poetic frequency harmonics...", (10, 100)),
        ("Teleporting to alternate thought zone...", (10, 100)),
        ("Dissecting your most recent daydream...", (10, 100)),
        ("Spooling cognitive trace logs...", (10, 100)),
        ("Slipping into subconscious sandbox...", (10, 100)),
        ("Running fantasy fingerprint scan...", (10, 100)),
        ("Extracting symbolic reasoning loops...", (10, 100)),
        ("Scanning sarcasm signature...", (10, 100)),
        ("Counting wild hypothetical tangents...", (10, 100)),
        ("Uploading guess to your memory stream...", (10, 100)),
        ("Connecting to intuition cloud...", (10, 100)),
        ("Warming up the sixth sense engine...", (10, 100)),
        ("Reconciling inner contradictions...", (10, 100)),
        ("Poking at unconscious memories...", (10, 100)),
        ("Detecting vague suspicion fields...", (10, 100)),
        ("Normalizing creative wavelengths...", (10, 100)),
        ("Sorting thoughts from emotional static...", (10, 100)),
        ("Buzzing your mental inbox...", (10, 100)),
        ("Summoning imagination sprites...", (10, 100)),
        ("Tuning your metaphoric frequency...", (10, 100)),
        ("Amplifying daydream resonance...", (10, 100)),
        ("Charging neuro-predictive battery...", (10, 100)),
        ("Sniffing out wishful thinking trails...", (10, 100)),
        ("Balancing logic vs instinct ratio...", (10, 100)),
        ("Greasing the gears of intuition...", (10, 100)),
        ("Inspecting your internal headcanon...", (10, 100)),
        ("Clarifying subconscious doodles...", (10, 100)),
        ("Polishing imaginary possibilities...", (10, 100)),
        ("Thinning ego interference...", (500, 700)),
        ("Unraveling deep thought entanglements...", (10, 100)),
        ("Shuffling abstract concept cards...", (10, 100)),
        ("Plucking stray dream fragments...", (10, 100)),
        ("Tapping into philosophical surge...", (10, 100)),
        ("Searching cerebral search history...", (10, 100)),
        ("Rendering speculative logic cloud...", (10, 100)),
        ("Verifying psychic checksum integrity...", (10, 100)),
        ("Adjusting internal belief compass...", (10, 100)),
        ("Sweeping the brains back alley...", (500, 700)),
        ("Cross-checking subliminal footnotes...", (500, 700)),
        ("Finalizing intuitive download...", (3000, 6000)),
        (f"You were thinking of {number}!", (0, 0))
    ]

    total_delay = 0
    for msg, (min_d, max_d) in messages:
        delay = random.randint(min_d, max_d)
        total_delay += delay
        root.after(total_delay, lambda m=msg: result_label.config(text=m))

    root.after(total_delay + 500, lambda: button.config(state='normal'))

button.config(command=guess_number)

#---------- Keeps the window open ----------#
root.mainloop()