SELECT data, reg_ans, descricao, SUM(vl_saldo_final) FROM intuitivecare_test3.demonstracoes_contabeis
WHERE YEAR(data) = YEAR(CURDATE())-1 and descricao = '"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "' and vl_saldo_final < 0
GROUP BY reg_ans
ORDER BY SUM(vl_saldo_final) ASC
LIMIT 10;