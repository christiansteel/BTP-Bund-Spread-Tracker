import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True,
                              gridspec_kw={"height_ratios": [3, 1]})

end = pd.Timestamp(dt.today() - timedelta(365))
df = df[df["date"] > end]

ax.plot(df["date"], df["Spread"])

ax.set_title("BTP-Bund Yield Spread", pad=24)

last_date = df["date"].iloc[-1].strftime("%d-%m-%Y")
last_value = df["Spread"].iloc[-1]
ax.text(0.5, 1.03, f"Latest Spread ({last_date}): {last_value} bp",
        transform=ax.transAxes, ha="center", fontsize=8, color="grey")

ax.set_ylabel("Spread (bp)")

# Bottom: z-score
ax2.plot(df["date"], df["Z-score"])
ax2.axhline(0, color="grey", linewidth=0.6)
ax2.set_ylabel("Z-score (60d)")

# Formatting shared by both 
for a in (ax, ax2):
    a.yaxis.tick_right()
    a.yaxis.set_label_position("right")
    a.grid(linewidth=1, alpha=0.3)
    a.spines[["top", "left"]].set_visible(False)
    a.spines[["bottom", "right"]].set_alpha(0.15)

ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))

fig.text(0.01, 0.01, "Source: bonds-api.com.", fontsize=8, color="grey")
fig.text(0.625, 0.01, "N.B. The data source provided month end values June and July", fontsize=8, color="grey")

fig.tight_layout(rect=(0, 0.02, 1, 1))
fig.savefig("BTP-Bund.png", dpi=150)
plt.show()
