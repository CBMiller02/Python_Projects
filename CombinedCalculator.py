# This is the personal budgeting application.

# Federal tax income brackets are 10, 12, 22, 24, 32, 35, and 37 percent.

income = float(input("What is your yearly taxable income?: $"))
print("\nWhat state do you live in? Type the full state name (i.e. 'California', 'Florida', 'Washington DC', etc.)")
state = input("State: ")
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# States income tax rates are calculated below:

# Alabama
if income >= 3000:
    al_tax = income - (income * 0.05)
elif income >= 500:
    al_tax = income - (income * 0.04)
elif income >= 0:
    al_tax = income
else:
    print("Not a valid input.")

# Alaska (no state income tax)
ak_tax = income

# Arizona
az_tax = income - (income * 0.025)

# Arkansas
if income >= 4500:
    ar_tax = income - (income * 0.039)
elif income >= 0:
    ar_tax = income - (income *0.02)
else:
    print("Not a valid input.")

#California
if income >= 1000000:
    ca_tax = income - (income * 0.1330)
elif income >= 721314:
    ca_tax = income - (income * 0.1230)
elif income >= 432787:
    ca_tax = income - (income * 0.1130)
elif income >= 360659:
    ca_tax = income - (income * 0.1030)
elif income >= 70606:
    ca_tax = income - (income * 0.093)
elif income >= 55866:
    ca_tax = income - (income * 0.08)
elif income >= 40245:
    ca_tax = income - (income * 0.06)
elif income >= 25499:
    ca_tax = income - (income * 0.04)
elif income >= 10756:
    ca_tax = income - (income * 0.02)
if income >= 0:
    ca_tax = income - (income * 0.01)
else:
    print("Not a valid input.")

# Colorado
co_tax = income - (income * 0.044)

# Connecticut
if income >= 500000:
    ct_tax = income - (income * 0.0699)
elif income >= 250000:
    ct_tax = income - (income * 0.0690)
elif income >= 200000:
    ct_tax = income - (income * 0.065)
elif income >= 100000:
    ct_tax = income - (income * 0.06)
elif income >= 50000:
    ct_tax = income - (income * 0.055)
elif income >= 10000:
    ct_tax = income - (income * 0.045)
elif income >= 0:
    ct_tax = income - (income * 0.02)
else:
    print("Not a valid input.")

# Delaware
if income >= 60000:
    de_tax = income - (income * 0.0660)
elif income >= 25000:
    de_tax = income - (income * 0.0555)
elif income >= 20000:
    de_tax = income - (income * 0.0520)
elif income >= 10000:
    de_tax = income - (income * 0.0480)
elif income >= 5000:
    de_tax = income - (income * 0.039)
elif income >= 2000:
    de_tax = income - (income * 0.022)
elif income >= 0:
    de_tax = income
else:
    print("Not a valid input.")

# Florida (no state income tax)
fl_tax = income

# Georgia
ga_tax = income - (income * 0.0539)

# Hawaii
if income >= 325000:
    hi_tax = income - (income * 0.11)
elif income >= 275000:
    hi_tax = income - (income * 0.1)
elif income >= 225000:
    hi_tax = income - (income * 0.0900)
elif income >= 175000:
    hi_tax = income - (income * 0.0825)
elif income >= 125000:
    hi_tax = income - (income * 0.0790)
elif income >= 48000:
    hi_tax = income - (income * 0.0760)
elif income >= 36000:
    hi_tax = income - (income * 0.0720)
elif income >= 24000:
    hi_tax = income - (income * 0.0680)
elif income >= 19200:
    hi_tax = income - (income * 0.0640)
elif income >= 14400:
    hi_tax = income - (income * 0.0550)
elif income >= 9600:
    hi_tax = income - (income * 0.0320)
elif income >= 0:
    hi_tax = income - (income * 0.0140)
else:
    print("Not a valid input.")

# Idaho
id_tax = income - (income *0.05695)

# Illinois
il_tax = income - (income * 0.0495)

# Indiana
in_tax = income - (income * 0.0300)

# Iowa
ia_tax = income - (income * 0.038)

# Kansas
if income >= 23000:
    ks_tax = income - (income * 0.0558)
elif income >= 0:
    ks_tax = income - (income * 0.0520)
else:
    print("Not a valid input.")

# Kentucky
ky_tax = income - (income * 0.0400)

# Louisiana
la_tax = income - (income * 0.0300)

# Maine
if income >= 63450:
    me_tax = income - (income * 0.0715)
elif income >= 26800:
    me_tax = income - (income * 0.0675)
elif income >= 0:
    me_tax = income - (income * 0.0580)
else:
    print("Not a valid input.")

# Maryland
if income >= 250000:
    md_tax = income - (income * 0.0575)
elif income >= 150000:
    md_tax = income - (income * 0.055)
elif income >= 125000:
    md_tax = income - (income * 0.0525)
elif income >= 100000:
    md_tax = income - (income * 0.05)
elif income >= 3000:
    md_tax = income - (income * 0.0475)
elif income >= 2000:
    md_tax = income - (income * 0.04)
elif income >= 1000:
    md_tax = income - (income * 0.03)
elif income >= 0:
    md_tax = income - (income * 0.02)
else:
    print("Not a valid input.")

# Massachusetts
if income >= 1083150:
    ma_tax = income - (income * 0.09)
elif income >= 0:
    ma_tax = income - (income * 0.05)
else:
    print("Not a valid input.")

# Michigan
mi_tax = income - (income * 0.0425)

# Minnesota
if income >= 198630:
    mn_tax = income - (income * 0.0985)
elif income >= 106990:
    mn_tax = income - (income * 0.0785)
elif income >= 32570:
    mn_tax = income - (income * 0.0680)
elif income >= 0:
    mn_tax = income - (income * 0.0535)
else:
    print("Not a valid input.")

# Mississippi
ms_tax = income - (income * 0.0400)

# Missouri
if income >= 9191:
    mo_tax = income - (income * 0.047)
elif income >= 7878:
    mo_tax = income - (income * 0.0450)
elif income >= 6565:
    mo_tax = income - (income * 0.04)
elif income >= 5252:
    mo_tax = income - (income * 0.035)
elif income >= 3939:
    mo_tax = income - (income * 0.03)
elif income >= 2626:
    mo_tax = income - (income * 0.025)
elif income >= 1313:
    mo_tax = income - (income * 0.02)
elif income >= 0:
    mo_tax = income
else:
    print("Not a valid input.")

# Montana
if income >= 21100:
    mt_tax = income - (income * 0.0590)
elif income >= 0:
    mt_tax = income - (income * 0.0470)
else:
    print("Not a valid input.")

# Nebraska
if income >= 38870:
    ne_tax = income - (income * 0.0520)
elif income >= 24120:
    ne_tax = income - (income * 0.0501)
elif income >= 4030:
    ne_tax = income - (income * 0.0351)
elif income >= 0:
    ne_tax = income - (income * 0.246)
else:
    print("Not a valid input.")

#Nevada (no state income tax)
nv_tax = income

# New Hampshire (no state income tax)
nh_tax = income

# New Jersey
if income >= 1000000:
    nj_tax = income - (income * 0.08970)
elif income >= 500000:
    nj_tax = income - (income * 0.06370)
elif income >= 75000:
    nj_tax = income - (income * 0.05525)
elif income >= 40000:
    nj_tax = income - (income * 0.03500)
elif income >= 35000:
    nj_tax = income - (income * 0.02450)
elif income >= 20000:
    nj_tax = income - (income * 0.01750)
elif income >= 0:
    nj_tax = income - (income * 0.01400)
else:
    print("Not a valid input.")

# New Mexico
if income >= 210000:
    nm_tax = income - (income * 0.0590)
elif income >= 66500:
    nm_tax = income - (income * 0.0490)
elif income >= 33500:
    nm_tax = income - (income * 0.0470)
elif income >= 16500:
    nm_tax = income - (income * 0.0430)
elif income >= 5500:
    nm_tax = income - (income * 0.0320)
if income >= 0:
    nm_tax = income - (income * 0.015)
else:
    print("Not a valid input.")

# New York
if income >= 25000000:
    ny_tax = income - (income * 0.1090)
elif income >= 5000000:
    ny_tax = income - (income * 0.1030)
elif income >= 1077550:
    ny_tax = income - (income * 0.0965)
elif income >= 215400:
    ny_tax = income - (income * 0.0685)
elif income >= 80650:
    ny_tax = income - (income * 0.06)
elif income >= 13900:
    ny_tax = income - (income * 0.0550)
elif income >= 11700:
    ny_tax = income - (income * 0.0525)
elif income >= 8500:
    ny_tax = income - (income * 0.045)
elif income >= 0:
    ny_tax = income - (income * 0.04)
else:
    print("Not a valid input.")

# North Carolina
nc_tax = income - (income * 0.0399)

# North Dakota
if income >= 244825:
    nd_tax = income - (income * 0.0250)
elif income >= 48475:
    nd_tax = income - (income * 0.0195)
elif income >= 0:
    nd_tax = income
else:
    print("Not a valid input.")

# Ohio
if income >= 100000:
    oh_tax = income - (income * 0.03500)
elif income >= 26050:
    oh_tax = income - (income * 0.02750)
elif income >= 0:
    oh_tax = income
else:
    print("Not a valid input.")

# Oklahoma
if income >= 7200:
    ok_tax = income - (income * 0.0475)
elif income >= 4900:
    ok_tax = income - (income * 0.0375)
elif income >= 3750:
    ok_tax = income - (income * 0.0275)
elif income >= 2500:
    ok_tax = income - (income * 0.0175)
elif income >= 1000:
    ok_tax = income - (income * 0.0075)
elif income >= 0:
    ok_tax = income - (income * 0.0025)
else:
    print("Not a valid input.")

# Oregon
if income >= 125000:
    or_tax = income - (income * 0.0990)
elif income >= 11050:
    or_tax = income - (income * 0.0875)
elif income >= 4400:
    or_tax = income - (income * 0.0675)
elif income >= 0:
    or_tax = income - (income * 0.0475)
else:
    print("Not a valid input.")

# Pennsylvania
pa_tax = income - (income * 0.0307)

# Rhode Island
if income >= 181650:
    ri_tax = income - (income * 0.0599)
elif income >= 79900:
    ri_tax = income - (income * 0.0475)
elif income >= 0:
    ri_tax = income - (income * 0.0375)
else:
    print("Not a valid input.")

# South Carolina
if income >= 17830:
    sc_tax = income - (income * 0.0620)
elif income >= 3560:
    sc_tax = income - (income * 0.0300)
elif income >= 0:
    sc_tax = income
else:
    print("Not a valid input.")

# South Dakota (no state income tax)
sd_tax = income

# Tennessee (no state income tax)
tn_tax = income

# Texas (no state income tax)
tx_tax = income

# Utah
ut_tax = income - (income * 0.0450)

# Vermont
if income >= 242000:
    vt_tax = income - (income * 0.0875)
elif income >= 116000:
    vt_tax = income - (income * 0.0760)
elif income >= 47900:
    vt_tax = income - (income * 0.0660)
elif income >= 0:
    vt_tax = income - (income * 0.0335)
else:
    print("Not a valid input.")

# Virginia
if income >= 17000:
    va_tax = income - (income * 0.0575)
elif income >= 5000:
    va_tax = income - (income * 0.05)
elif income >= 3000:
    va_tax = income - (income * 0.03)
elif income >= 0:
    va_tax = income - (income * 0.02)
else:
    print("Not a valid input.")

# Washington (no state income tax)
wa_tax = income

# West Virginia
if income >= 60000:
    wv_tax = income - (income * 0.0482)
elif income >= 40000:
    wv_tax = income - (income * 0.0444)
elif income >= 25000:
    wv_tax = income - (income * 0.0333)
elif income >= 10000:
    wv_tax = income - (income * 0.0296)
elif income >= 0:
    wv_tax = income - (income * 0.0222)
else:
    print("Not a valid input.")

# Wisconsin
if income >= 323290:
    wi_tax = income - (income * 0.0765)
elif income >= 29370:
    wi_tax = income - (income * 0.0530)
elif income >= 14680:
    wi_tax = income - (income * 0.0440)
elif income >= 0:
    wi_tax = income - (income * 0.0350)
else:
    print("Not a valid input.")

# Wyoming (no state income tax)
wy_tax = income

# Washington DC
if income >= 1000000:
    dc_tax = income - (income * 0.1075)
elif income >= 500000:
    dc_tax = income - (income * 0.0975)
elif income >= 250000:
    dc_tax = income - (income * 0.0925)
elif income >= 60000:
    dc_tax = income - (income * 0.0850)
elif income >= 40000:
    dc_tax = income - (income * 0.0650)
elif income >= 10000:
    dc_tax = income - (income * 0.06)
elif income >= 0:
    dc_tax = income - (income * 0.04)
else:
    print("Not a valid input.")

# ------------------------------------------------

if state == "Alabama":
    state_income = al_tax
elif state == "Alaska":
    state_income = ak_tax
elif state == "Arizona":
    state_income = az_tax
elif state == "Arkansas":
    state_income = ar_tax
elif state == "California":
    state_income = ca_tax
elif state == "Colorado":
    state_income = co_tax
elif state == "Connecticut":
    state_income = ct_tax
elif state == "Delaware":
    state_income = de_tax
elif state == "Florida":
    state_income = fl_tax
elif state == "Georgia":
    state_income = ga_tax
elif state == "Hawaii":
    state_income = hi_tax
elif state == "Idaho":
    state_income = id_tax
elif state == "Illinois":
    state_income = il_tax
elif state == "Indiana":
    state_income = in_tax
elif state == "Iowa":
    state_income = ia_tax
elif state == "Kansas":
    state_income = ks_tax
elif state == "Kentucky":
    state_income = ky_tax
elif state == "Louisiana":
    state_income = la_tax
elif state == "Maine":
    state_income = me_tax
elif state == "Maryland":
    state_income = md_tax
elif state == "Massachusetts":
    state_income = ma_tax
elif state == "Michigan":
    state_income = mi_tax
elif state == "Minnesota":
    state_income = mn_tax
elif state == "Mississippi":
    state_income = ms_tax
elif state == "Missouri":
    state_income = mo_tax
elif state == "Montana":
    state_income = mt_tax
elif state == "Nebraska":
    state_income = ne_tax
elif state == "Nevada":
    state_income = nv_tax
elif state == "New Hampshire":
    state_income = nh_tax
elif state == "New Jersey":
    state_income = nj_tax
elif state == "New Mexico":
    state_income = nm_tax
elif state == "New York":
    state_income = ny_tax
elif state == "North Carolina":
    state_income = nc_tax
elif state == "North Dakota":
    state_income = nd_tax
elif state == "Ohio":
    state_income = oh_tax
elif state == "Oklahoma":
    state_income = ok_tax
elif state == "Oregon":
    state_income = or_tax
elif state == "Pennsylvania":
    state_income = pa_tax
elif state == "Rhode Island":
    state_income = ri_tax
elif state == "South Carolina":
    state_income = sc_tax
elif state == "South Dakota":
    state_income = sd_tax
elif state == "Tennessee":
    state_income = tn_tax
elif state == "Texas":
    state_income = tx_tax
elif state == "Utah":
    state_income = ut_tax
elif state == "Vermont":
    state_income = vt_tax
elif state == "Virginia":
    state_income = va_tax
elif state == "Washington":
    state_income = wa_tax
elif state == "West Virginia":
    state_income = wv_tax
elif state == "Wisconsin":
    state_income = wi_tax
elif state == "Wyoming":
    state_income = wy_tax
elif state == "Washington DC":
    state_income = dc_tax
else:
    print("State not found.")
    state_income = income

# Federal income tax calculation

if state_income <= 12400:
    post_federal_income = state_income - (state_income * 0.10)

elif state_income <= 50400:
    post_federal_income = state_income - (state_income * 0.12)

elif state_income <= 105700:
    post_federal_income = state_income - (state_income * 0.22)

elif state_income <= 201775:
    post_federal_income = state_income - (state_income * 0.24)

elif state_income <= 256225:
    post_federal_income = state_income - (state_income * 0.32)

elif state_income <= 640600:
    post_federal_income = state_income - (state_income * 0.35)

elif state_income > 640600:
    post_federal_income = state_income - (state_income * 0.37)

else:
    print("That is not a valid income.")


print("$", post_federal_income, "is your Yearly take home pay, after state income tax and federal income tax.")
print("$", (post_federal_income / 12), "is your Monthly post-tax, take-home pay.")

# Convert yearly after-tax income into monthly after-tax income.

monthly_income = post_federal_income / 12


# Now we will move on to the budget.

print("This is your personal budget calculator.")

house = int(input("Enter your monthly rent or mortgage: $"))
groceries = int(input("Enter your monthly grocery spending: $"))
phone = int(input("Enter your monthly phone bill: $"))
internet = int(input("Enter your monthly internet bill: $"))
car_payment = int(input("Enter your monthly car payment: $"))
car_insurance = int(input("Enter your monthly car insurance: $"))
car_maint = int(input("Enter your monthly car maintenance: $"))
health = int(input("Enter your monthly health insurance: $"))
prop = int(input("Enter your monthly renters OR property insurance: $"))

total_expenses = (house + groceries + phone + internet + car_payment + car_insurance + car_maint + health + prop)
print("$", total_expenses, "is the sum of your monthly expenses.")

# Moving on to combine income and taxes.

leftover = (monthly_income - total_expenses)
print("$", leftover, "is how much you have left, after paying US + Pennsylvania taxes and paying expenses.")

# Now we know how much is left over. Let's allocate budgeting.

print("Now we will allocate the remainder savings. Combined percentage cannot exceed 100%.")
print("We will cover 4 savings sections: Retirement Savings, Family, Travel, and Miscallaneous.")
savings = int(input("What percentage of your leftover money would you like to save for retirement? %"))
family = int(input("What percentage of your leftover money would you like to save for family needs or events? %"))
travel = int(input("What percentage of your leftover money would you like to save for travel? %"))
misc = int(input("What percentage of your leftover money would you like to save for miscellaneous items? %"))

total = savings + family + travel + misc

if total > 100:
    print("The amount you entered exceeds 100%. Please adjust the amounts.")

elif total >= 0:
    print("Thank you for your input. The sum of what you will save is: $", total)

else:
    print("That is not a valid input.")