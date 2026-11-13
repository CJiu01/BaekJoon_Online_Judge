select count(*)
from ECOLI_DATA
where (GENOTYPE & 2 = 0) & (GENOTYPE & 5 > 0)