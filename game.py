import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!", color="black", size=20)
    resposta_correta = "Gato"
    page.bgcolor = "#FFD700"
    

    def verificar_reposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabéns🎉🎉👏"
        else:
            mensagem.value = "Resposta errada❌❌"
        page.update()
             

    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
       ft.Column(
           controls=[
               ft.Text(
                   "Adivinhe a Imagem",
                   size=24,
                   weight="bold",
                   color = "black"
               ),
               ft.Image(
                   src="images/gatinho.jpg",
                   height=200
               ),
               ft.Row(
                   controls=[
                       ft.ElevatedButton(
                           content="Cachorro",
                           on_click=verificar_reposta
                       ),
                       ft.ElevatedButton(
                           content="Gato",
                           on_click=verificar_reposta
                       ),
                       ft.ElevatedButton(
                           content="Coelho",
                           on_click=verificar_reposta
                       ),
                   ],
                    alignment = ft.MainAxisAlignment.CENTER
               ),
               mensagem
           ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
       )
    )

ft.run(main)