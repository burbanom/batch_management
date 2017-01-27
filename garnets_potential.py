# Oxygen charge
charge_o = FORCEFIELD.CHARGE_add()
charge_o.Atom = "O"
charge_o.Charge = -2.0000

# Lithium charge
charge_li = FORCEFIELD.CHARGE_add()
charge_li.Atom = "Li"
charge_li.Charge = 1.0000

# Lanthanum charge
charge_la = FORCEFIELD.CHARGE_add()
charge_la.Atom = "La"
charge_la.Charge = 3.0000

# Aluminium charge
charge_al = FORCEFIELD.CHARGE_add()
charge_al.Atom = "Al"
charge_al.Charge = 3.0000

# Gallium charge
charge_ga = FORCEFIELD.CHARGE_add()
charge_ga.Atom = "Ga"
charge_ga.Charge = 3.0000

# Scandium charge
charge_sc = FORCEFIELD.CHARGE_add()
charge_sc.Atom = "Sc"
charge_sc.Charge = 3.0000

# Zirconium charge
charge_zr = FORCEFIELD.CHARGE_add()
charge_zr.Atom = "Zr"
charge_zr.Charge = 4.0000

# Niobium charge
charge_nb = FORCEFIELD.CHARGE_add()
charge_nb.Atom = "Nb"
charge_nb.Charge = 5.0000

# Tantalum charge
charge_ta = FORCEFIELD.CHARGE_add()
charge_ta.Atom = "Ta"
charge_ta.Charge = 5.0000

# Dipole interactions
#################################
### Oxygen dipole ###############
dipole_o = FORCEFIELD.DIPOLE_add()
dipole_o.Atom = "O"
dipole_o.Apol = 2.0701731
### O-O damping #################
ddamp_oo = dipole_o.DAMPING_add()
ddamp_oo.Order = 4
ddamp_oo.Type = "Tang-Toennies"
ddamp_oo.Atom = "O"
ddamp_oo.Bij = 4.3317333
ddamp_oo.Cij = 3.9405919
### O-M damping #################
ddamp_oli = dipole_o.DAMPING_add()
ddamp_oli.Order = 4
ddamp_oli.Type = "Tang-Toennies"
ddamp_oli.Atom = "Li"
ddamp_oli.Bij = 3.3456379
ddamp_oli.Cij = 1.3714911
###################################
ddamp_ola = dipole_o.DAMPING_add()
ddamp_ola.Order = 4
ddamp_ola.Type = "Tang-Toennies"
ddamp_ola.Atom = "La"
ddamp_ola.Bij = 3.1835987
ddamp_ola.Cij = 1.8785859
###################################
ddamp_oal = dipole_o.DAMPING_add()
ddamp_oal.Order = 4
ddamp_oal.Type = "Tang-Toennies"
ddamp_oal.Atom = "Al"
ddamp_oal.Bij = 3.4333484
ddamp_oal.Cij = 1.4024422
###################################
ddamp_oga = dipole_o.DAMPING_add()
ddamp_oga.Order = 4
ddamp_oga.Type = "Tang-Toennies"
ddamp_oga.Atom = "Ga"
ddamp_oga.Bij = 3.5138778
ddamp_oga.Cij = 1.4649098
###################################
ddamp_osc = dipole_o.DAMPING_add()
ddamp_osc.Order = 4
ddamp_osc.Type = "Tang-Toennies"
ddamp_osc.Atom = "Sc"
ddamp_osc.Bij = 3.4046317
ddamp_osc.Cij = 1.5197859
###################################
ddamp_ozr = dipole_o.DAMPING_add()
ddamp_ozr.Order = 4
ddamp_ozr.Type = "Tang-Toennies"
ddamp_ozr.Atom = "Zr"
ddamp_ozr.Bij = 3.4132512
ddamp_ozr.Cij = 1.6693846
###################################
ddamp_onb = dipole_o.DAMPING_add()
ddamp_onb.Order = 4
ddamp_onb.Type = "Tang-Toennies"
ddamp_onb.Atom = "Nb"
ddamp_onb.Bij = 3.7173205
ddamp_onb.Cij = 1.7391378
###################################
ddamp_ota = dipole_o.DAMPING_add()
ddamp_ota.Order = 4
ddamp_ota.Type = "Tang-Toennies"
ddamp_ota.Atom = "Ta"
ddamp_ota.Bij = 3.4663382
ddamp_ota.Cij = 1.4680228

### Lanthanum dipole ###############
dipole_la = FORCEFIELD.DIPOLE_add()
dipole_la.Atom = "La"
dipole_la.Apol = 1.1128848
### La-O damping #################
ddamp_lao = dipole_la.DAMPING_add()
ddamp_lao.Order = 4
ddamp_lao.Type = "Tang-Toennies"
ddamp_lao.Atom = "O"
ddamp_lao.Bij = ddamp_ola.Bij
ddamp_lao.Cij = 0.0277657
###################################

### Scandium dipole ###############
dipole_sc = FORCEFIELD.DIPOLE_add()
dipole_sc.Atom = "Sc"
dipole_sc.Apol = 0.2519200
### Sc-O damping #################
ddamp_sco = dipole_sc.DAMPING_add()
ddamp_sco.Order = 4
ddamp_sco.Type = "Tang-Toennies"
ddamp_sco.Atom = "O"
ddamp_sco.Bij = ddamp_osc.Bij
ddamp_sco.Cij = -0.8447576
###################################

### Zirconium dipole ###############
dipole_zr = FORCEFIELD.DIPOLE_add()
dipole_zr.Atom = "Zr"
dipole_zr.Apol = 0.3526900
### Zr-O damping #################
ddamp_zro = dipole_zr.DAMPING_add()
ddamp_zro.Order = 4
ddamp_zro.Type = "Tang-Toennies"
ddamp_zro.Atom = "O"
ddamp_zro.Bij = ddamp_ozr.Bij
ddamp_zro.Cij = -0.6497141
###################################

### Niobium dipole ###############
dipole_nb = FORCEFIELD.DIPOLE_add()
dipole_nb.Atom = "Nb"
dipole_nb.Apol = 0.2921500
### Nb-O damping #################
ddamp_nbo = dipole_nb.DAMPING_add()
ddamp_nbo.Order = 4
ddamp_nbo.Type = "Tang-Toennies"
ddamp_nbo.Atom = "O"
ddamp_nbo.Bij = ddamp_onb.Bij 
ddamp_nbo.Cij = -0.1466152
###################################

### Tantalum dipole ###############
dipole_ta = FORCEFIELD.DIPOLE_add()
dipole_ta.Atom = "Ta"
dipole_ta.Apol = 0.2784000
### Ta-O damping #################
ddamp_tao = dipole_ta.DAMPING_add()
ddamp_tao.Order = 4
ddamp_tao.Type = "Tang-Toennies"
ddamp_tao.Atom = "O"
ddamp_tao.Bij = ddamp_ota.Bij 
ddamp_tao.Cij = -0.1466152
###################################


# O-O BMHFTD 
bmhftd_oo = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_oo.Atoms = ["O", "O"]
bmhftd_oo.A = 9.8974116 
bmhftd_oo.B = 4.0455752
bmhftd_oo.C = 1.8226524200680616
bmhftd_oo.D = 7.625161753143967
bmhftd_oo.Bd = 2.4566310140216943

# O-Li BMHFTD 
bmhftd_oli = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_oli.Atoms = ["O", "Li"]
bmhftd_oli.A = 17.6719475
bmhftd_oli.B = 3.2139797
bmhftd_oli.C = 0.0 
bmhftd_oli.D = 0.0 
bmhftd_oli.Bd = 0.0 

# O-La BMHFTD 
bmhftd_ola = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_ola.Atoms = ["O", "La"]
bmhftd_ola.A = 69.3050783
bmhftd_ola.B = 2.8601297
bmhftd_ola.C = 1.2517079384139898
bmhftd_ola.D = 4.4951558399582581
bmhftd_ola.Bd = 2.7589856003628257

# O-Al BMHFTD 
bmhftd_oal = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_oal.Atoms = ["O", "Al"]
bmhftd_oal.A = 36.7871944
bmhftd_oal.B = 3.0600582
bmhftd_oal.C = 0.0 
bmhftd_oal.D = 0.0 
bmhftd_oal.Bd = 0.0 

# O-Ga BMHFTD 
bmhftd_oga = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_oga.Atoms = ["O", "Ga"]
bmhftd_oga.A = 50.7580798
bmhftd_oga.B = 3.1616374
bmhftd_oga.C = 0.0 
bmhftd_oga.D = 0.0 
bmhftd_oga.Bd = 0.0 

# O-Sc BMHFTD 
bmhftd_osc = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_osc.Atoms = ["O", "Sc"]
bmhftd_osc.A = 63.3769522
bmhftd_osc.B = 3.1410621
bmhftd_osc.C = 0.3293910471081182
bmhftd_osc.D = 1.2114168269107755
bmhftd_osc.Bd = 3.3447976113987686

# O-Zr BMHFTD 
bmhftd_ozr = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_ozr.Atoms = ["O", "Zr"]
bmhftd_ozr.A = 57.9642311
bmhftd_ozr.B = 2.8812672
bmhftd_ozr.C = 0.46114746595136552
bmhftd_ozr.D = 1.6664668025016252
bmhftd_ozr.Bd = 3.0613401867039576

# O-Nb BMHFTD 
bmhftd_onb = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_onb.Atoms = ["O", "Nb"]
bmhftd_onb.A = 44.1029098
bmhftd_onb.B = 2.6679943
bmhftd_onb.C = 0.387166236770 
bmhftd_onb.D = 1.382060567757 
bmhftd_onb.Bd = 3.51487206622

# O-Ta BMHFTD 
bmhftd_ota = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_ota.Atoms = ["O", "Ta"]
bmhftd_ota.A = 59.3278675
bmhftd_ota.B = 2.8412481
bmhftd_ota.C = 0.382774356143
bmhftd_ota.D = 1.36693323073
bmhftd_ota.Bd = 3.51487206622

# La-La BMHFTD 
bmhftd_lala = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lala.Atoms = ["La", "La"]
bmhftd_lala.A = 1.00000000000E-04
bmhftd_lala.B = 9.4485808231603627
bmhftd_lala.C = 0.0 
bmhftd_lala.D = 0.0 
bmhftd_lala.Bd = 0.0 

# La-Li BMHFTD 
bmhftd_lali = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lali.Atoms = ["La", "Li"]
bmhftd_lali.A = 1.00000000000E-04
bmhftd_lali.B = 9.4485808231603627
bmhftd_lali.C = 0.0 
bmhftd_lali.D = 0.0 
bmhftd_lali.Bd = 0.0 

# La-Al BMHFTD 
bmhftd_laal = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_laal.Atoms = ["La", "Al"]
bmhftd_laal.A = 1.00000000000E-04
bmhftd_laal.B = 9.4485808231603627
bmhftd_laal.C = 0.0 
bmhftd_laal.D = 0.0 
bmhftd_laal.Bd = 0.0 

# La-Ga BMHFTD 
bmhftd_laga = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_laga.Atoms = ["La", "Ga"]
bmhftd_laga.A = 1.00000000000E-04
bmhftd_laga.B = 9.4485808231603627
bmhftd_laga.C = 0.0 
bmhftd_laga.D = 0.0 
bmhftd_laga.Bd = 0.0 

# La-Sc BMHFTD 
bmhftd_lasc = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lasc.Atoms = ["La", "Sc"]
bmhftd_lasc.A = 1.00000000000E-04
bmhftd_lasc.B = 9.4485808231603627
bmhftd_lasc.C = 0.0 
bmhftd_lasc.D = 0.0 
bmhftd_lasc.Bd = 0.0 

# La-Zr BMHFTD 
bmhftd_lazr = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lazr.Atoms = ["La", "Zr"]
bmhftd_lazr.A = 1.00000000000E-04
bmhftd_lazr.B = 9.4485808231603627
bmhftd_lazr.C = 0.0 
bmhftd_lazr.D = 0.0 
bmhftd_lazr.Bd = 0.0 

# La-Nb BMHFTD 
bmhftd_lanb = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lanb.Atoms = ["La", "Nb"]
bmhftd_lanb.A = 1.00000000000E-04
bmhftd_lanb.B = 9.4485808231603627
bmhftd_lanb.C = 0.0 
bmhftd_lanb.D = 0.0 
bmhftd_lanb.Bd = 0.0 

# La-Ta BMHFTD 
bmhftd_lata = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lata.Atoms = ["La", "Nb"]
bmhftd_lata.A = 1.00000000000E-04
bmhftd_lata.B = 9.4485808231603627
bmhftd_lata.C = 0.0 
bmhftd_lata.D = 0.0 
bmhftd_lata.Bd = 0.0 

# Al-Al BMHFTD 
bmhftd_alal = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alal.Atoms = ["Al", "Al"]
bmhftd_alal.A = 1.00000000000E-04
bmhftd_alal.B = 9.4485808231603627
bmhftd_alal.C = 0.0 
bmhftd_alal.D = 0.0 
bmhftd_alal.Bd = 0.0 

# Al-Li BMHFTD 
bmhftd_alli = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alli.Atoms = ["Al", "Li"]
bmhftd_alli.A = 1.00000000000E-04
bmhftd_alli.B = 9.4485808231603627
bmhftd_alli.C = 0.0 
bmhftd_alli.D = 0.0 
bmhftd_alli.Bd = 0.0 

# Al-Ga BMHFTD 
bmhftd_alga = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alga.Atoms = ["Al", "Ga"]
bmhftd_alga.A = 1.00000000000E-04
bmhftd_alga.B = 9.4485808231603627
bmhftd_alga.C = 0.0 
bmhftd_alga.D = 0.0 
bmhftd_alga.Bd = 0.0 

# Al-Sc BMHFTD 
bmhftd_alsc = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alsc.Atoms = ["Al", "Sc"]
bmhftd_alsc.A = 1.00000000000E-04
bmhftd_alsc.B = 9.4485808231603627
bmhftd_alsc.C = 0.0 
bmhftd_alsc.D = 0.0 
bmhftd_alsc.Bd = 0.0 

# Al-Zr BMHFTD 
bmhftd_alzr = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alzr.Atoms = ["Al", "Zr"]
bmhftd_alzr.A = 1.00000000000E-04
bmhftd_alzr.B = 9.4485808231603627
bmhftd_alzr.C = 0.0 
bmhftd_alzr.D = 0.0 
bmhftd_alzr.Bd = 0.0 

# Al-Nb BMHFTD 
bmhftd_alnb = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alnb.Atoms = ["Al", "Nb"]
bmhftd_alnb.A = 1.00000000000E-04
bmhftd_alnb.B = 9.4485808231603627
bmhftd_alnb.C = 0.0 
bmhftd_alnb.D = 0.0 
bmhftd_alnb.Bd = 0.0 

# Al-Ta BMHFTD 
bmhftd_alta = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_alta.Atoms = ["Al", "Ta"]
bmhftd_alta.A = 1.00000000000E-04
bmhftd_alta.B = 9.4485808231603627
bmhftd_alta.C = 0.0 
bmhftd_alta.D = 0.0 
bmhftd_alta.Bd = 0.0 

# Ga-Ga BMHFTD 
bmhftd_gaga = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_gaga.Atoms = ["Ga", "Ga"]
bmhftd_gaga.A = 1.00000000000E-04
bmhftd_gaga.B = 9.4485808231603627
bmhftd_gaga.C = 0.0 
bmhftd_gaga.D = 0.0 
bmhftd_gaga.Bd = 0.0 

# Ga-Li BMHFTD 
bmhftd_gali = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_gali.Atoms = ["Ga", "Li"]
bmhftd_gali.A = 1.00000000000E-04
bmhftd_gali.B = 9.4485808231603627
bmhftd_gali.C = 0.0 
bmhftd_gali.D = 0.0 
bmhftd_gali.Bd = 0.0 

# Ga-Sc BMHFTD 
bmhftd_gasc = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_gasc.Atoms = ["Ga", "Sc"]
bmhftd_gasc.A = 1.00000000000E-04
bmhftd_gasc.B = 9.4485808231603627
bmhftd_gasc.C = 0.0 
bmhftd_gasc.D = 0.0 
bmhftd_gasc.Bd = 0.0 

# Sc-Sc BMHFTD 
bmhftd_scsc = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_scsc.Atoms = ["Sc", "Sc"]
bmhftd_scsc.A = 1.00000000000E-04
bmhftd_scsc.B = 9.4485808231603627
bmhftd_scsc.C = 0.0 
bmhftd_scsc.D = 0.0 
bmhftd_scsc.Bd = 0.0 

# Sc-Li BMHFTD 
bmhftd_scli = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_scli.Atoms = ["Sc", "Li"]
bmhftd_scli.A = 1.00000000000E-04
bmhftd_scli.B = 9.4485808231603627
bmhftd_scli.C = 0.0 
bmhftd_scli.D = 0.0 
bmhftd_scli.Bd = 0.0 

# Zr-Zr BMHFTD 
bmhftd_zrzr = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_zrzr.Atoms = ["Zr", "Zr"]
bmhftd_zrzr.A = 1.00000000000E-04
bmhftd_zrzr.B = 9.4485808231603627
bmhftd_zrzr.C = 0.0 
bmhftd_zrzr.D = 0.0 
bmhftd_zrzr.Bd = 0.0 

# Zr-Li BMHFTD 
bmhftd_zrli = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_zrli.Atoms = ["Zr", "Li"]
bmhftd_zrli.A = 1.00000000000E-04
bmhftd_zrli.B = 9.4485808231603627
bmhftd_zrli.C = 0.0 
bmhftd_zrli.D = 0.0 
bmhftd_zrli.Bd = 0.0 

# Zr-Ga BMHFTD 
bmhftd_zrga = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_zrga.Atoms = ["Zr", "Ga"]
bmhftd_zrga.A = 1.00000000000E-04
bmhftd_zrga.B = 9.4485808231603627
bmhftd_zrga.C = 0.0 
bmhftd_zrga.D = 0.0 
bmhftd_zrga.Bd = 0.0 

# Zr-Sc BMHFTD 
bmhftd_zrsc = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_zrsc.Atoms = ["Zr", "Sc"]
bmhftd_zrsc.A = 1.00000000000E-04
bmhftd_zrsc.B = 9.4485808231603627
bmhftd_zrsc.C = 0.0 
bmhftd_zrsc.D = 0.0 
bmhftd_zrsc.Bd = 0.0 

# Zr-Nb BMHFTD 
bmhftd_zrnb = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_zrnb.Atoms = ["Zr", "Nb"]
bmhftd_zrnb.A = 1.00000000000E-04
bmhftd_zrnb.B = 9.4485808231603627
bmhftd_zrnb.C = 0.0 
bmhftd_zrnb.D = 0.0 
bmhftd_zrnb.Bd = 0.0 

# Nb-Nb BMHFTD 
bmhftd_nbnb = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_nbnb.Atoms = ["Nb", "Nb"]
bmhftd_nbnb.A = 1.00000000000E-04
bmhftd_nbnb.B = 9.4485808231603627
bmhftd_nbnb.C = 0.0 
bmhftd_nbnb.D = 0.0 
bmhftd_nbnb.Bd = 0.0 

# Ta-Ta BMHFTD 
bmhftd_tata = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_tata.Atoms = ["Ta", "Ta"]
bmhftd_tata.A = 1.00000000000E-04
bmhftd_tata.B = 9.4485808231603627
bmhftd_tata.C = 0.0 
bmhftd_tata.D = 0.0 
bmhftd_tata.Bd = 0.0 

# Li-Li BMHFTD 
bmhftd_lili = FORCEFIELD.NONBONDED.BMHFTD_add()
bmhftd_lili.Atoms = ["Li", "Li"]
bmhftd_lili.A = 1.00000000000E-04
bmhftd_lili.B = 9.4485808231603627
bmhftd_lili.C = 0.0 
bmhftd_lili.D = 0.0 
bmhftd_lili.Bd = 0.0 

o_kind = SUBSYS.KIND_add("O")
o_kind.Element = "O"
o_kind.Mass = 15.9994 

li_kind = SUBSYS.KIND_add("Li")
li_kind.Element = "Li"
li_kind.Mass = 6.94

la_kind = SUBSYS.KIND_add("La")
la_kind.Element = "La"
la_kind.Mass = 138.91 

al_kind = SUBSYS.KIND_add("Al")
al_kind.Element = "Al"
al_kind.Mass = 26.981539

ga_kind = SUBSYS.KIND_add("Ga")
ga_kind.Element = "Ga"
ga_kind.Mass = 69.723 

sc_kind = SUBSYS.KIND_add("Sc")
sc_kind.Element = "Sc"
sc_kind.Mass = 44.955912

zr_kind = SUBSYS.KIND_add("Zr")
zr_kind.Element = "Zr"
zr_kind.Mass = 91.224 

nb_kind = SUBSYS.KIND_add("Nb")
nb_kind.Element = "Nb"
nb_kind.Mass = 92.90638

ta_kind = SUBSYS.KIND_add("Ta")
ta_kind.Element = "Ta"
ta_kind.Mass = 180.94788

