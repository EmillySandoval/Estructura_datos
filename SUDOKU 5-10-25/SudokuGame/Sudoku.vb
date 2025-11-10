Imports System
Imports System.Collections.Generic
Imports System.IO
Imports System.Linq

Public Class Sudoku
    Private _tablero(8, 8) As Integer
    Private _tableroInicial(8, 8) As Integer
    Private _vidas As Integer
    Private _nivelActual As Integer
    Private _victoriasEnNivelActual As Integer
    Private _victoriasNecesarias As Integer = 5

    ' Configuración de niveles
    Private _configuracionNiveles As New Dictionary(Of Integer, Tuple(Of Integer, Integer)) From {
        {1, New Tuple(Of Integer, Integer)(36, 44)},
        {2, New Tuple(Of Integer, Integer)(32, 35)},
        {3, New Tuple(Of Integer, Integer)(28, 31)},
        {4, New Tuple(Of Integer, Integer)(24, 27)},
        {5, New Tuple(Of Integer, Integer)(17, 24)}
    }

    Public Sub New()
        _vidas = 5
        _nivelActual = 1
        _victoriasEnNivelActual = 0
    End Sub

    Public Sub NuevoJuego()
        _vidas = 5
        GenerarNuevoPuzzle()
    End Sub

    Private Sub GenerarNuevoPuzzle()
        ' Limpiar tableros
        Array.Clear(_tablero, 0, _tablero.Length)
        Array.Clear(_tableroInicial, 0, _tableroInicial.Length)

        ' Generar solución completa
        ResolverSudoku(_tablero)

        ' Quitar números según el nivel
        QuitarNumerosParaNivel()

        ' Copiar al tablero inicial
        Array.Copy(_tablero, _tableroInicial, _tablero.Length)
    End Sub

    Private Sub QuitarNumerosParaNivel()
        Dim rand As New Random()
        Dim nivel = _configuracionNiveles(_nivelActual)
        Dim numerosAMantener = rand.Next(nivel.Item1, nivel.Item2 + 1)
        Dim numerosAQuitar = 81 - numerosAMantener

        Dim posiciones As New List(Of Tuple(Of Integer, Integer))()
        For i As Integer = 0 To 8
            For j As Integer = 0 To 8
                posiciones.Add(New Tuple(Of Integer, Integer)(i, j))
            Next
        Next

        ' Mezclar posiciones
        posiciones = posiciones.OrderBy(Function(x) rand.Next()).ToList()

        ' Quitar números
        For i As Integer = 0 To numerosAQuitar - 1
            _tablero(posiciones(i).Item1, posiciones(i).Item2) = 0
        Next
    End Sub

    Private Function ResolverSudoku(ByRef grid(,) As Integer) As Boolean
        For fila As Integer = 0 To 8
            For columna As Integer = 0 To 8
                If grid(fila, columna) = 0 Then
                    Dim numeros = Enumerable.Range(1, 9).OrderBy(Function(x) Guid.NewGuid()).ToList()

                    For Each num As Integer In numeros
                        If EsMovimientoValido(grid, fila, columna, num) Then
                            grid(fila, columna) = num

                            If ResolverSudoku(grid) Then
                                Return True
                            End If

                            grid(fila, columna) = 0
                        End If
                    Next
                    Return False
                End If
            Next
        Next
        Return True
    End Function

    Public Function EsMovimientoValido(grid(,) As Integer, fila As Integer, columna As Integer, numero As Integer) As Boolean
        ' Verificar fila
        For i As Integer = 0 To 8
            If grid(fila, i) = numero Then Return False
        Next

        ' Verificar columna
        For i As Integer = 0 To 8
            If grid(i, columna) = numero Then Return False
        Next

        ' Verificar caja 3x3
        Dim inicioFila As Integer = fila - fila Mod 3
        Dim inicioColumna As Integer = columna - columna Mod 3
        For i As Integer = 0 To 2
            For j As Integer = 0 To 2
                If grid(inicioFila + i, inicioColumna + j) = numero Then Return False
            Next
        Next

        Return True
    End Function

    Public Function ColocarNumero(fila As Integer, columna As Integer, numero As Integer) As Boolean
        If _tableroInicial(fila, columna) <> 0 Then
            Return False ' No se puede modificar números iniciales
        End If

        If Not EsMovimientoValido(_tablero, fila, columna, numero) AndAlso numero <> 0 Then
            _vidas -= 1
            Return False
        End If

        _tablero(fila, columna) = numero
        Return True
    End Function

    Public Function VerificarVictoria() As Boolean
        ' Verificar que no hay celdas vacías
        For i As Integer = 0 To 8
            For j As Integer = 0 To 8
                If _tablero(i, j) = 0 Then
                    Return False
                End If
            Next
        Next

        ' Verificar que todas las filas, columnas y cajas sean válidas
        For i As Integer = 0 To 8
            If Not EsFilaValida(i) OrElse Not EsColumnaValida(i) Then
                Return False
            End If
        Next

        For i As Integer = 0 To 8 Step 3
            For j As Integer = 0 To 8 Step 3
                If Not EsCajaValida(i, j) Then
                    Return False
                End If
            Next
        Next

        Return True
    End Function

    Private Function EsFilaValida(fila As Integer) As Boolean
        Dim numeros As New HashSet(Of Integer)()
        For columna As Integer = 0 To 8
            If _tablero(fila, columna) <> 0 Then
                If numeros.Contains(_tablero(fila, columna)) Then
                    Return False
                End If
                numeros.Add(_tablero(fila, columna))
            End If
        Next
        Return True
    End Function

    Private Function EsColumnaValida(columna As Integer) As Boolean
        Dim numeros As New HashSet(Of Integer)()
        For fila As Integer = 0 To 8
            If _tablero(fila, columna) <> 0 Then
                If numeros.Contains(_tablero(fila, columna)) Then
                    Return False
                End If
                numeros.Add(_tablero(fila, columna))
            End If
        Next
        Return True
    End Function

    Private Function EsCajaValida(inicioFila As Integer, inicioColumna As Integer) As Boolean
        Dim numeros As New HashSet(Of Integer)()
        For i As Integer = 0 To 2
            For j As Integer = 0 To 2
                Dim num As Integer = _tablero(inicioFila + i, inicioColumna + j)
                If num <> 0 Then
                    If numeros.Contains(num) Then
                        Return False
                    End If
                    numeros.Add(num)
                End If
            Next
        Next
        Return True
    End Function

    Public Sub SubirNivel()
        _victoriasEnNivelActual += 1
        If _victoriasEnNivelActual >= _victoriasNecesarias AndAlso _nivelActual < 5 Then
            _nivelActual += 1
            _victoriasEnNivelActual = 0
        End If
    End Sub

    ' Propiedades para acceder desde el formulario
    Public ReadOnly Property TableroActual As Integer(,)
        Get
            Return _tablero
        End Get
    End Property

    Public ReadOnly Property TableroInicial As Integer(,)
        Get
            Return _tableroInicial
        End Get
    End Property

    Public ReadOnly Property VidasRestantes As Integer
        Get
            Return _vidas
        End Get
    End Property

    Public ReadOnly Property NivelActual As Integer
        Get
            Return _nivelActual
        End Get
    End Property

    Public ReadOnly Property VictoriasEnNivelActual As Integer
        Get
            Return _victoriasEnNivelActual
        End Get
    End Property

    Public ReadOnly Property NombreNivel As String
        Get
            Return ObtenerNombreNivel(_nivelActual)
        End Get
    End Property

    Private Function ObtenerNombreNivel(nivel As Integer) As String
        Select Case nivel
            Case 1 : Return "MUY FÁCIL"
            Case 2 : Return "FÁCIL"
            Case 3 : Return "MEDIO"
            Case 4 : Return "DIFÍCIL"
            Case 5 : Return "MUY DIFÍCIL"
            Case Else : Return "DESCONOCIDO"
        End Select
    End Function

    Public Sub GuardarJuego(rutaArchivo As String)
        Try
            Using escritor As New StreamWriter(rutaArchivo)
                ' Guardar estado del juego
                escritor.WriteLine(_nivelActual)
                escritor.WriteLine(_victoriasEnNivelActual)
                escritor.WriteLine(_vidas)

                ' Guardar tablero actual
                For i As Integer = 0 To 8
                    For j As Integer = 0 To 8
                        escritor.Write(_tablero(i, j) & " ")
                    Next
                    escritor.WriteLine()
                Next

                ' Guardar tablero inicial
                For i As Integer = 0 To 8
                    For j As Integer = 0 To 8
                        escritor.Write(_tableroInicial(i, j) & " ")
                    Next
                    escritor.WriteLine()
                Next
            End Using
        Catch ex As Exception
            Throw New Exception("Error al guardar el juego: " & ex.Message)
        End Try
    End Sub

    Public Sub CargarJuego(rutaArchivo As String)
        Try
            Using lector As New StreamReader(rutaArchivo)
                _nivelActual = Integer.Parse(lector.ReadLine())
                _victoriasEnNivelActual = Integer.Parse(lector.ReadLine())
                _vidas = Integer.Parse(lector.ReadLine())

                ' Cargar tablero actual
                For i As Integer = 0 To 8
                    Dim valores As String() = lector.ReadLine().Split(" "c)
                    For j As Integer = 0 To 8
                        _tablero(i, j) = Integer.Parse(valores(j))
                    Next
                Next

                ' Cargar tablero inicial
                For i As Integer = 0 To 8
                    Dim valores As String() = lector.ReadLine().Split(" "c)
                    For j As Integer = 0 To 8
                        _tableroInicial(i, j) = Integer.Parse(valores(j))
                    Next
                Next
            End Using
        Catch ex As Exception
            Throw New Exception("Error al cargar el juego: " & ex.Message)
        End Try
    End Sub
End Class