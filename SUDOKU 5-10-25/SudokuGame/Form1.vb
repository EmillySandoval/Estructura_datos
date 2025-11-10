Imports System.Drawing
Imports System.Windows.Forms

Public Class Form1
    Private juego As Sudoku
    Private cajasTexto(8, 8) As TextBox
    Private Const ARCHIVO_GUARDADO As String = "sudoku_guardado.txt"

    ' Controles
    Private etiquetaNivel As Label
    Private etiquetaVictorias As Label
    Private etiquetaVidas As Label
    Private botonGuardar As Button
    Private botonNuevoJuego As Button

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        InicializarControles()
        InicializarJuego()
    End Sub

    Private Sub InicializarControles()
        ' Configuración del formulario
        Me.Text = "SUDOCU - Juego de Sudoku"
        Me.Size = New Size(550, 700) ' Aumenté el tamaño para el nuevo diseño
        Me.StartPosition = FormStartPosition.CenterScreen
        Me.BackColor = Color.White

        ' Etiqueta de nivel
        etiquetaNivel = New Label()
        With etiquetaNivel
            .Location = New Point(20, 20)
            .Size = New Size(250, 25)
            .Font = New Font("Arial", 12, FontStyle.Bold)
            .ForeColor = Color.DarkBlue
            .Text = "NIVEL: CARGANDO..."
        End With
        Me.Controls.Add(etiquetaNivel)

        ' Etiqueta de victorias
        etiquetaVictorias = New Label()
        With etiquetaVictorias
            .Location = New Point(20, 50)
            .Size = New Size(150, 20)
            .Font = New Font("Arial", 10)
            .Text = "Victorias: 0/5"
        End With
        Me.Controls.Add(etiquetaVictorias)

        ' Etiqueta de vidas
        etiquetaVidas = New Label()
        With etiquetaVidas
            .Location = New Point(200, 50)
            .Size = New Size(150, 20)
            .Font = New Font("Arial", 10)
            .ForeColor = Color.Red
            .Text = "Vidas: 5"
        End With
        Me.Controls.Add(etiquetaVidas)

        ' Botón Guardar
        botonGuardar = New Button()
        With botonGuardar
            .Location = New Point(400, 20)
            .Size = New Size(100, 30)
            .Text = "Guardar"
            .BackColor = Color.LightGreen
            .Font = New Font("Arial", 9, FontStyle.Bold)
        End With
        Me.Controls.Add(botonGuardar)
        AddHandler botonGuardar.Click, AddressOf BotonGuardar_Click

        ' Botón Nueva Partida
        botonNuevoJuego = New Button()
        With botonNuevoJuego
            .Location = New Point(400, 600)
            .Size = New Size(100, 30)
            .Text = "Nueva Partida"
            .BackColor = Color.LightBlue
            .Font = New Font("Arial", 9, FontStyle.Bold)
        End With
        Me.Controls.Add(botonNuevoJuego)
        AddHandler botonNuevoJuego.Click, AddressOf BotonNuevoJuego_Click

        ' Crear el tablero
        CrearTablero()
    End Sub

    Private Sub CrearTablero()
        Dim tamanoCelda As Integer = 40
        Dim inicioX As Integer = 30
        Dim inicioY As Integer = 100
        Dim grosorLineaGruesa As Integer = 3

        For fila As Integer = 0 To 8
            For columna As Integer = 0 To 8
                Dim cajaTexto As New TextBox()
                With cajaTexto
                    .Name = $"txtCelda_{fila}_{columna}"
                    .Width = tamanoCelda
                    .Height = tamanoCelda

                    ' Ajustar posición con separaciones para cajas 3x3
                    Dim separacionExtraX As Integer = If(columna >= 3, grosorLineaGruesa, 0) + If(columna >= 6, grosorLineaGruesa, 0)
                    Dim separacionExtraY As Integer = If(fila >= 3, grosorLineaGruesa, 0) + If(fila >= 6, grosorLineaGruesa, 0)

                    .Location = New Point(inicioX + columna * tamanoCelda + separacionExtraX,
                                         inicioY + fila * tamanoCelda + separacionExtraY)

                    .TextAlign = HorizontalAlignment.Center
                    .Font = New Font("Arial", 14, FontStyle.Bold)
                    .Tag = $"{fila},{columna}"
                    .MaxLength = 1 ' Solo un carácter
                    .BorderStyle = BorderStyle.FixedSingle
                End With

                AddHandler cajaTexto.KeyPress, AddressOf Celda_KeyPress
                AddHandler cajaTexto.TextChanged, AddressOf Celda_TextChanged

                cajasTexto(fila, columna) = cajaTexto
                Me.Controls.Add(cajaTexto)
            Next
        Next

        ' Agregar líneas gruesas para separar las cajas 3x3
        AgregarLineasSeparadoras(inicioX, inicioY, tamanoCelda, grosorLineaGruesa)
    End Sub

    Private Sub AgregarLineasSeparadoras(inicioX As Integer, inicioY As Integer, tamanoCelda As Integer, grosor As Integer)
        ' Líneas verticales gruesas
        For i As Integer = 1 To 2
            Dim lineaVertical As New Panel()
            With lineaVertical
                .Width = grosor
                .Height = tamanoCelda * 9 + grosor * 2
                .BackColor = Color.Black
                .Location = New Point(inicioX + tamanoCelda * 3 * i + grosor * (i - 1), inicioY)
            End With
            Me.Controls.Add(lineaVertical)
            lineaVertical.SendToBack()
        Next

        ' Líneas horizontales gruesas
        For i As Integer = 1 To 2
            Dim lineaHorizontal As New Panel()
            With lineaHorizontal
                .Width = tamanoCelda * 9 + grosor * 2
                .Height = grosor
                .BackColor = Color.Black
                .Location = New Point(inicioX, inicioY + tamanoCelda * 3 * i + grosor * (i - 1))
            End With
            Me.Controls.Add(lineaHorizontal)
            lineaHorizontal.SendToBack()
        Next
    End Sub

    Private Sub InicializarJuego()
        juego = New Sudoku()

        ' Preguntar si quiere cargar juego guardado
        If IO.File.Exists(ARCHIVO_GUARDADO) Then
            Dim resultado = MessageBox.Show("¿Deseas cargar la partida guardada?", "Sudoku",
                                            MessageBoxButtons.YesNo, MessageBoxIcon.Question)

            If resultado = DialogResult.Yes Then
                Try
                    juego.CargarJuego(ARCHIVO_GUARDADO)
                    ActualizarPantalla()
                Catch ex As Exception
                    MessageBox.Show("Error al cargar: " & ex.Message, "Error",
                                    MessageBoxButtons.OK, MessageBoxIcon.Error)
                    juego.NuevoJuego()
                    ActualizarPantalla()
                End Try
            Else
                juego.NuevoJuego()
                ActualizarPantalla()
            End If
        Else
            juego.NuevoJuego()
            ActualizarPantalla()
        End If
    End Sub

    Private Sub ActualizarPantalla()
        If juego Is Nothing Then Return

        ' Actualizar información del nivel y vidas
        etiquetaNivel.Text = "NIVEL: " & juego.NombreNivel
        etiquetaVictorias.Text = "Victorias: " & juego.VictoriasEnNivelActual & "/5"
        etiquetaVidas.Text = "Vidas: " & juego.VidasRestantes

        ' Actualizar el tablero visual
        For fila As Integer = 0 To 8
            For columna As Integer = 0 To 8
                If cajasTexto(fila, columna) Is Nothing Then Continue For

                Dim valor As Integer = juego.TableroActual(fila, columna)
                Dim valorInicial As Integer = juego.TableroInicial(fila, columna)

                ' Evitar que el evento TextChanged se dispare mientras actualizamos
                RemoveHandler cajasTexto(fila, columna).TextChanged, AddressOf Celda_TextChanged
                cajasTexto(fila, columna).Text = If(valor = 0, "", valor.ToString())
                AddHandler cajasTexto(fila, columna).TextChanged, AddressOf Celda_TextChanged

                ' Números iniciales en negro, números del usuario en azul
                If valorInicial <> 0 Then
                    cajasTexto(fila, columna).ForeColor = Color.Black
                    cajasTexto(fila, columna).BackColor = Color.LightGray
                    cajasTexto(fila, columna).ReadOnly = True
                    cajasTexto(fila, columna).Font = New Font("Arial", 14, FontStyle.Bold)
                Else
                    cajasTexto(fila, columna).ForeColor = Color.Blue
                    cajasTexto(fila, columna).BackColor = Color.White
                    cajasTexto(fila, columna).ReadOnly = False
                    cajasTexto(fila, columna).Font = New Font("Arial", 14, FontStyle.Regular)
                End If
            Next
        Next

        ' Verificar si perdió
        If juego.VidasRestantes <= 0 Then
            MessageBox.Show("¡Has perdido todas tus vidas! Comenzando nuevo juego...",
                            "Game Over", MessageBoxButtons.OK, MessageBoxIcon.Information)
            juego.NuevoJuego()
            ActualizarPantalla()
        End If
    End Sub

    Private Sub Celda_KeyPress(sender As Object, e As KeyPressEventArgs)
        ' Solo permitir números del 1-9 y tecla borrar
        If Not Char.IsControl(e.KeyChar) AndAlso Not Char.IsDigit(e.KeyChar) Then
            e.Handled = True
        ElseIf Char.IsDigit(e.KeyChar) AndAlso (e.KeyChar < "1"c OrElse e.KeyChar > "9"c) Then
            e.Handled = True
        End If
    End Sub

    Private Sub Celda_TextChanged(sender As Object, e As EventArgs)
        Dim cajaTexto As TextBox = CType(sender, TextBox)
        If String.IsNullOrEmpty(cajaTexto.Tag?.ToString()) Then Return

        Dim partes() As String = cajaTexto.Tag.ToString().Split(","c)
        If partes.Length < 2 Then Return

        Dim fila As Integer = Integer.Parse(partes(0))
        Dim columna As Integer = Integer.Parse(partes(1))

        If cajaTexto.Text.Length > 0 Then
            Dim numero As Integer
            If Integer.TryParse(cajaTexto.Text, numero) Then
                Dim movimientoValido As Boolean = juego.ColocarNumero(fila, columna, numero)

                If Not movimientoValido Then
                    MessageBox.Show("¡Movimiento inválido! Pierdes una vida.", "Error",
                                    MessageBoxButtons.OK, MessageBoxIcon.Warning)
                End If

                ActualizarPantalla()

                ' Verificar si ganó
                If juego.VerificarVictoria() Then
                    MessageBox.Show("¡Felicidades! Has completado el nivel " & juego.NivelActual,
                                    "¡Victoria!", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)

                    juego.SubirNivel()
                    juego.NuevoJuego()
                    ActualizarPantalla()
                End If
            End If
        Else
            ' Si borró el número, poner 0
            juego.ColocarNumero(fila, columna, 0)
        End If
    End Sub

    Private Sub BotonGuardar_Click(sender As Object, e As EventArgs)
        Try
            juego.GuardarJuego(ARCHIVO_GUARDADO)
            MessageBox.Show("Partida guardada correctamente.", "Guardado",
                            MessageBoxButtons.OK, MessageBoxIcon.Information)
        Catch ex As Exception
            MessageBox.Show("Error al guardar: " & ex.Message, "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try
    End Sub

    Private Sub BotonNuevoJuego_Click(sender As Object, e As EventArgs)
        Dim resultado = MessageBox.Show("¿Estás seguro de que quieres empezar una nueva partida?",
                                        "Nueva Partida", MessageBoxButtons.YesNo, MessageBoxIcon.Question)

        If resultado = DialogResult.Yes Then
            juego.NuevoJuego()
            ActualizarPantalla()
        End If
    End Sub
End Class