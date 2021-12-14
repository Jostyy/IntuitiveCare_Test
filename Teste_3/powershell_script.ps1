#Loading multiple csv files using windows's powershell
$escape = '\"'
$files = Get-ChildItem path -Recurse *.csv
foreach($f in $files){
mysql -e "
     	load data infile 'path\\$f' into table demonstracoes_contabeis
	character set latin1
	fields terminated by ';' 
	ignore 1 lines 
	(@data, @reg_ans, @cd_conta_contabil, descricao, @vl_saldo_final) 
	set 
		data = str_to_date(replace(replace(@data,'$escape',''),'/','-'),'%d-%m-%Y'), 
		reg_ans = replace(@reg_ans,'$escape',''), 
		cd_conta_contabil = replace(@cd_conta_contabil, '$escape', ''), 
		vl_saldo_final = replace(replace(@vl_saldo_final,'$escape',''),',','.')" -u myusername --password=mypassword database 
}

Write-Host -NoNewLine 'Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
