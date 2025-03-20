base = """"""
# albania.addEventListener('click', () => {
#     console.log("Albania!!!")
#     changeElementColor(albania)
#     guess[0] = albania
#     guess[1] = "Albania"
# });
ctxt = """Albania  Andorra  Austria  Belarus  Belgium  Bosnia and Herzegovina  Bulgaria  Croatia  Czechia  Denmark  Estonia  Finland  France  Germany  Greece  Hungary  Iceland  Ireland  Italy  Latvia  Liechtenstein  Lithuania  Luxembourg  Malta  Moldova  Monaco  Montenegro  Netherlands  North Macedonia  Norway  Poland  Portugal  Romania  Russia  San Marino  Serbia  Slovakia  Slovenia  Spain  Sweden  Switzerland  The Vatican  Ukraine  United Kingdom"""
clist = ctxt.split("  ")

# ctxt2 = """Albania  Andorra  Austria  Belarus  Belgium  Bosnia and Herzegovina  Bulgaria  Croatia  Czechia  Denmark  Estonia  Finland  France  Germany  Greece  Hungary  Iceland  Ireland  Italy  Latvia  Liechtenstein  Lithuania  Luxembourg  Malta  Moldova  Monaco  Montenegro Netherlands  North Macedonia  Norway  Poland  Portugal  Romania  Russia  San Marino  Serbia  Slovakia  Slovenia  Spain  Sweden  Switzerland  The Vatican  Ukraine  United Kingdom"""
# clist2 = ctxt2.split("  ")
# # # for i in clist:
# #     print(f"const {i.lower().replace(" ","_")} = document.getElementById('{i}');")
length = 0
for i in clist:
    var = i.lower().replace(" ","_")
    name = i
    print(f"""{var}.addEventListener('click', () => {{
    console.log("{name}!!!")
    changeElementColor(guess, {var})
    guess[0] = {var}
    guess[1] = "{name}"
    updateFeedback('{name}')
}});""")
    length += 1