fig, ax = plt.subplots() 
ax.plot(df['date'], df['Spread'])

ax.set_title("BTP-Bund Yield Spread", pad=24)

ax.set_ylabel('Spread (bp)')
ax.yaxis.tick_right()            
ax.yaxis.set_label_position("right") 

ax.grid(linewidth = 1,alpha=0.3)

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))

fig.text(0.01, 0.01, "Source: bonds-api.com.", fontsize=8, color="grey")

last_date = df["date"].iloc[-1]
last_date = last_date.strftime("%d-%m-%Y")
last_value = df["Spread"].iloc[-1]

fig.text(0.345, 0.9, f"Latest Spread ({last_date}): {last_value} bp", fontsize=8, color="grey")
ax.spines[["top", "left"]].set_visible(False)
ax.spines[["bottom", "right"]].set_alpha(0.15)

plt.show()
