from tkinter import *
from tkinter import ttk
class Generator():
	def __init__(self):
		self.setup()

	def generate(self):
		allow = True
		try:
			valueMinLength = int(self.minLength.get())
			valueMaxLength = int(self.maxLength.get())
			valueCondition = str(self.condition.get())
			valueSameOnLeft = bool(self.mapping.get())
			valueTrials = int(self.trials.get())
			if valueMaxLength <= valueMinLength:
				self.popupmsg("Maximum value must be larger than minimum value", "Warning")
				allow = False
			elif valueTrials%10 != 0:
				allow = False
				self.popupmsg("Trial number must be a multiple of 10", "Warning")

		except ValueError:
			self.popupmsg("Enter values in all fields", "Warning")
		if allow:
			self.popupmsg("Running stimulus generation code", "Stimulus Generator")


	def popupmsg(self, msg, title):
		popup = Toplevel(self.root)
		popup.wm_title(title)
		popup.tkraise(self.root)
		Label(popup, text=msg).pack(side="top", fill="x", pady=10, padx = 15)
		Button(popup, text="Okay", command = popup.destroy).pack(pady=10)

	def setup(self):
		self.root = Tk()
		self.root.title("Stimulus Generator")

		mainframe = ttk.Frame(self.root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		self.root.columnconfigure(0, weight=1)
		self.root.rowconfigure(0, weight=1)


		self.minLength = IntVar(mainframe, value=2)
		ttk.Label(mainframe, text="Minimum Stimulus Dimension:").grid(column=1, row=1, sticky=W)
		minLength_entry = ttk.Entry(mainframe, width=7, textvariable=self.minLength)
		minLength_entry.grid(column=2, row=1, sticky=(W, E))

		self.maxLength = IntVar(mainframe, value=25)
		ttk.Label(mainframe, text="Maximum Stimulus Dimension:").grid(column=1, row=2, sticky=W)
		maxLength_entry = ttk.Entry(mainframe, width=7, textvariable=self.maxLength)
		maxLength_entry.grid(column=2, row=2, sticky=(W, E))

		self.condition = StringVar(mainframe, "difference")
		ttk.Label(mainframe, text="Condition:").grid(column=1, row=3, sticky=W)
		condition_entry = ttk.Radiobutton(mainframe, text="Difference", variable=self.condition, value="difference").grid(column=2, row=3, sticky=(W))
		condition_entry = ttk.Radiobutton(mainframe, text="Ratio", variable=self.condition, value="ratio").grid(column=3, row=3, sticky=(W))

		self.mapping = StringVar(mainframe, True)
		ttk.Label(mainframe, text="Mapping:").grid(column=1, row=4, sticky=W)
		condition_entry = ttk.Radiobutton(mainframe, text="Same -> Different", variable=self.mapping, value=True).grid(column=2, row=4, sticky=(W))
		condition_entry = ttk.Radiobutton(mainframe, text="Different -> Same", variable=self.mapping, value=False).grid(column=3, row=4, sticky=(W))

		self.trials = IntVar(mainframe, value=50)
		ttk.Label(mainframe, text="Number of trials per block:").grid(column=1, row=5, sticky=W)
		trials_entry = ttk.Entry(mainframe, width=7, textvariable=self.trials)
		trials_entry.grid(column=2, row=5, sticky=(W, E))

		genBtn = ttk.Button(mainframe, text="Generate", command=self.generate).grid(column=3, row=6, sticky=W)

		for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

		self.root.bind('<Return>', self.generate)
		self.root.bind('<Escape>', lambda e: self.root.destroy())


# use input values to generate stimulus set

# write stimulus set to csv

# write info file to txt


# START APP ##########################################################################################################
if __name__ == "__main__":
	generator = Generator()
	try:
		generator.root.mainloop()
	except (KeyboardInterrupt, SystemExit):
		raise