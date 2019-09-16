# get input:
    # X minLength = 2
    # X maxLength = 25 
    # - must be larger than min length 
    # X numberOfTrials 
    # X default = 50 
    # <must be multiple of 10, (i.e. number of bins is 10)>
    # X condition - choose "ratio" of "difference" (or mixed? - not yet implemented), 
    # X sameOnTheLeft - bool if True, most similar stimulus pairs will be mapped to the far left of the response bar (0) and least similar will be mapped to the far right (1)
    # if False, vice versa


# starting with a tk template

from tkinter import *
from tkinter import ttk

def generate(*args):
    allow = True
    try:
        valueMinLength = int(minLength.get())
        valueMaxLength = int(maxLength.get())
        if valueMaxLength <= valueMinLength:
            print("Maximum value must be larger than minimum value")
            allow = False
        valueCondition = str(condition.get())
        valueSameOnLeft = bool(mapping.get())
        valueTrials = int(trials.get())
        if valueTrials%10 != 0:
            allow = False
            print("trial number must be a multiple of 10")

    except ValueError:
        print("enter values in all fields")
    if allow:
        print("Run stimulus generation code")

root = Tk()
root.title("Stimulus Generator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


minLength = IntVar(mainframe, value=2)
ttk.Label(mainframe, text="Minimum Stimulus Dimension:").grid(column=1, row=1, sticky=W)
minLength_entry = ttk.Entry(mainframe, width=7, textvariable=minLength)
minLength_entry.grid(column=2, row=1, sticky=(W, E))

maxLength = IntVar(mainframe, value=25)
ttk.Label(mainframe, text="Maximum Stimulus Dimension:").grid(column=1, row=2, sticky=W)
maxLength_entry = ttk.Entry(mainframe, width=7, textvariable=maxLength)
maxLength_entry.grid(column=2, row=2, sticky=(W, E))

condition = StringVar(mainframe, "difference")
ttk.Label(mainframe, text="Condition:").grid(column=1, row=3, sticky=W)
condition_entry = ttk.Radiobutton(mainframe, text="Difference", variable=condition, value="difference").grid(column=2, row=3, sticky=(W))
condition_entry = ttk.Radiobutton(mainframe, text="Ratio", variable=condition, value="ratio").grid(column=3, row=3, sticky=(W))

mapping = StringVar(mainframe, True)
ttk.Label(mainframe, text="Mapping:").grid(column=1, row=4, sticky=W)
condition_entry = ttk.Radiobutton(mainframe, text="Same -> Different", variable=mapping, value=True).grid(column=2, row=4, sticky=(W))
condition_entry = ttk.Radiobutton(mainframe, text="Different -> Same", variable=mapping, value=False).grid(column=3, row=4, sticky=(W))

trials = IntVar(mainframe, value=50)
ttk.Label(mainframe, text="Number of trials per block:").grid(column=1, row=5, sticky=W)
trials_entry = ttk.Entry(mainframe, width=7, textvariable=trials)
trials_entry.grid(column=2, row=5, sticky=(W, E))

genBtn = ttk.Button(mainframe, text="Generate", command=generate).grid(column=3, row=6, sticky=W)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# genBtn.focus()
root.bind('<Return>', generate)
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()


# write stim to csv

# write info file