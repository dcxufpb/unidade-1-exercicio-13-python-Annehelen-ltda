# coding: utf-8
def isEmpty(value:str) -> bool:
        return (value == None) or (len(value) == value.count(" "))


class Endereco:
  
  def __init__(self, logradouro, numero, complemento, bairro, municipio, 
      estado, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
  def endereco_info (self):
    self.validacao_endereco()
    numero = int()
    try:
      numero = int(self.numero)
    except Exception:
      numero = 0
    if(numero<=0):
      numero = "s/n"
    
    part2 = f"{self.logradouro}, {numero}"
    if not isEmpty (self.complemento):
      part2 += f" {self.complemento}"
    part3 = str()
    if not isEmpty (self.bairro):
        part3 += f"{self.bairro} - "
    part3 += f"{self.municipio} - {self.estado}"
    part4 = str()
    if not isEmpty (self.cep):
        part4 = f"CEP:{self.cep}"
   
    ende = f"{part2}\n"
    ende += f"{part3}\n"
    ende += f"{part4}"
    return ende
  
  def validacao_endereco (self):
    if (isEmpty(self.logradouro)):
      raise Exception("O campo logradouro do endereço é obrigatório")
    if (isEmpty(self.municipio)):
        raise Exception("O campo município do endereço é obrigatório")
    if (isEmpty(self.estado)):
        raise Exception("O campo estado do endereço é obrigatório")
    

class Loja:
  
  def __init__(self, nome_loja, endereco, telefone, observacao, cnpj, 
      inscricao_estadual):
    self.nome_loja = nome_loja
    self.endereco = endereco
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual
  
  def validacao_loja(self):
    if (isEmpty(self.nome_loja)):
      raise Exception("O campo nome da loja é obrigatório")
    if(isEmpty(self.cnpj)):
      raise Exception("O campo CNPJ da loja é obrigatório")
    if (isEmpty(self.inscricao_estadual)):
      raise Exception("O campo inscrição estadual da loja é obrigatório")

  def dados_loja(self):
    # Implemente aqui
    self.validacao_loja()

    part4 = self.endereco.endereco_info()

    if not isEmpty(self.telefone):
        if not isEmpty(self.endereco.cep):
            part4 += " "
        part4 += f"Tel {self.telefone}"     
    if not isEmpty(part4):
        part4 += "\n"
    part5 = str()
    if not isEmpty(self.observacao):
        part5 += f"{self.observacao}"
    
    loj = f"{self.nome_loja}\n"
    loj += f"{part4}"
    loj += f"{part5}\n"
    loj += f"CNPJ: {self.cnpj}\n"
    loj += f"IE: {self.inscricao_estadual}"
    
    return loj

class Venda:
  def __init__(self, loja, datahora, ccf, coo):
    self.loja = loja
    self.datahora = datahora
    self.ccf = ccf
    self.coo = coo
    self.itens = []

  def adicionar_item(self, item, codigo, descricao, quantidade, unidade, valor_unitario, substituicao_tributaria):
    item_venda = ItemVenda(self, item, codigo, descricao, quantidade, unidade, 
                     valor_unitario, substituicao_tributaria)
    self.itens.append(item_venda)

  def dados_venda(self):
    texto_data = self.datahora.strftime("%d/%m/%Y")
    texto_hora = self.datahora.time().strftime("%H:%M:%S")
    return '''{data} {hora}V CCF:{ccf} COO: {coo}'''.format(data=texto_data,
                                                            hora=texto_hora, 
                                                            ccf=self.ccf, 
                                                            coo=self.coo)
  def dados_itens(self):
    dados = ["ITEM CODIGO DESCRICAO QTD UN VL UNIT(R$) ST VL ITEM(R$)\n"]
    for item_linha in self.itens:
      valor_item = item_linha.quantidade * item_linha.valor_unitario
      linha = '''{item} {codigo} {descricao} {qtd} {un} {vl_unit:.2f} {st} {vl_item:.2f}
'''.format(item=item_linha.item, codigo=item_linha.codigo, 
           descricao=item_linha.descricao, qtd=item_linha.quantidade, 
           un=item_linha.unidade, vl_unit=item_linha.valor_unitario, 
           st=item_linha.substituicao_tributaria, vl_item=valor_item)
      dados.append(linha)
    return ''.join(dados)

  def calcular_total(self):
    totais = []
    for item_linha in self.itens:
      totais.append(item_linha.quantidade * item_linha.valor_unitario)
    return sum(totais)

  def imprimir_cupom(self):
    dados_loja = self.loja.dados_loja()
    dados_venda = self.dados_venda()
    dados_itens = self.dados_itens()
    total = self.calcular_total()

    cupons_dados = f"{dados_loja}\n"
    cupons_dados += f"{dados_venda}\n"
    cupons_dados += f"{dados_itens}\n"
    cupons_dados += f"{total}"
    return cupons_dados

  # Implemente aqui
