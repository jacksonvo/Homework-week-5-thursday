def get_at_content(dna, sig_figs): 
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round(at_content, sig_figs) 

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG", 1)
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"), 2)
print(get_at_content("aactgtagctagctagcagcgta"), 3)
