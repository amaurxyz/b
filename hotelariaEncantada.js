// Variáveis globais para armazenamento dos dados
let funcionarios = [{ nome: 'admin', senha: '1234', id: 1 }];  // Usuário padrão para testes
let hospedes = JSON.parse(localStorage.getItem('hospedes')) || [];
let reservas = JSON.parse(localStorage.getItem('reservas')) || [];
let operacoes = [];
let quartos = [
  { tipo: 'solteiro', preco: 100 },
  { tipo: 'casal', preco: 150 },
  { tipo: 'solteiro suite', preco: 200 },
  { tipo: 'casal suite', preco: 250 },
  { tipo: 'solteiro cobertura', preco: 300 },
  { tipo: 'casal cobertura', preco: 350 }
];

function listarClientesHospedados() {
  const listaHospedados = document.getElementById('listaHospedados');
  listaHospedados.innerHTML = '';
  reservas.forEach(reserva => {
    if (reserva.checkin) {
      const li = document.createElement('li');
      const hospede = hospedes.find(h => h.id === reserva.hospedeId);

      li.textContent = `Hóspede: ${hospede.nome}, Quarto: ${reserva.quartoNumero} (${reserva.tipoQuarto})`;
      listaHospedados.appendChild(li);
    }
  });
}

function exibirReservas() {
  const listaReservas = document.getElementById('listaReservas');
  listaReservas.innerHTML = '';
  reservas.forEach(reserva => {
    const li = document.createElement('li');
    const hospede = hospedes.find(h => h.id === reserva.hospedeId);

    li.textContent = `Id: ${reserva.id}, ${hospede.nome}, quarto de ${reserva.tipoQuarto}, duração da reserva: ${reserva.dias} dias, Data da Reserva: ${reserva.dataReserva}`;

    const btnCheckIn = document.createElement('button');
    btnCheckIn.textContent = 'Check-in';
    btnCheckIn.onclick = () => realizarCheckIn(reserva.hospedeId);

    const btnExcluirReserva = document.createElement('button');
    btnExcluirReserva.textContent = 'Excluir Reserva';
    btnExcluirReserva.onclick = () => excluirReserva(reserva.id);

    li.appendChild(btnCheckIn);
    li.appendChild(btnExcluirReserva);
    listaReservas.appendChild(li);
  });
}

function excluirReserva(reservaId) {
  reservas = reservas.filter(r => r.id !== reservaId);
  localStorage.setItem('reservas', JSON.stringify(reservas));
  alert('Reserva excluída com sucesso');
  exibirReservas();
}

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('listaReservas')) {
    exibirReservas();
  }
  if (document.getElementById('listaHospedados')) {
    listarClientesHospedados();
  }
  verificarAutenticacao(); // Verificar autenticação ao carregar a página
});

function autenticarFuncionario(nome, senha) {
  const funcionario = funcionarios.find(f => f.nome === nome && f.senha === senha);
  if (funcionario) {
    localStorage.setItem('funcionarioLogado', JSON.stringify(funcionario)); // Armazena o funcionário logado
    return true;
  }
  return false;
}

function verificarAutenticacao() {
  const funcionarioLogado = JSON.parse(localStorage.getItem('funcionarioLogado'));
  if (!funcionarioLogado) {
    window.location.href = 'index.html'; // Redireciona para a página de login
  }
}

document.addEventListener('DOMContentLoaded', () => {
  let frigobar = false;

  if (document.getElementById('login-form')) {
    document.getElementById('login-form').addEventListener('submit', event => {
      event.preventDefault();
      const nome = document.getElementById('funcionarioNome').value;
      const senha = document.getElementById('senha').value;

      const loginError = document.getElementById('loginError');
      loginError.classList.add('hidden'); // Esconder a mensagem de erro antes da tentativa de login

      if (autenticarFuncionario(nome, senha)) {
        window.location.href = 'listaHospedes.html';
      } else {
        loginError.classList.remove('hidden');
      }
    });
  }

  if (document.getElementById('cadastro-hospede-form')) {
    document.getElementById('cadastro-hospede-form').addEventListener('submit', event => {
      event.preventDefault();
      const dadosHospede = {
        nome: document.getElementById('nomeHospede').value,
        nascimento: document.getElementById('nascimento').value,
        cpf: document.getElementById('cpf').value,
        cep: document.getElementById('cep').value,
        rua: document.getElementById('rua').value,
        numero: document.getElementById('numero').value,
        email: document.getElementById('email').value,
        telefone: document.getElementById('telefone').value
      };
      cadastrarHospede(dadosHospede);
      alert('Hóspede cadastrado com sucesso');
      document.getElementById('cadastro-hospede-form').reset();
    });
  }

  if (document.getElementById('listaHospedes')) {
    exibirHospedes();
  }

  if (document.getElementById('reservas-form')) {
    document.getElementById('reservas-form').addEventListener('submit', event => {
      event.preventDefault();
      const hospedeSelecionado = document.getElementById('HospedeSelecionado').value;
      const tipoQuarto = document.getElementById('tipoQuarto').value;
      const precoQuarto = parseFloat(document.getElementById('precoQuarto').value);
      const dias = parseInt(document.getElementById('dias').value);
      const quartoNumero = document.getElementById('quartoNumero').value;
      const funcionario = JSON.parse(localStorage.getItem('funcionarioLogado'));
      const funcionarioId = funcionario ? funcionario.id : null;

      reservarQuarto(parseInt(hospedeSelecionado), tipoQuarto, funcionarioId, precoQuarto, dias, quartoNumero);
      document.getElementById('reservas-form').reset();
    });

    const hospedeSelect = document.getElementById('HospedeSelecionado');
    hospedes.forEach(h => {
      const option = document.createElement('option');
      option.value = h.id;
      option.textContent = `${h.nome} (ID: ${h.id})`;  // Corrigir aqui
      hospedeSelect.appendChild(option);
   });
  }

  if (document.getElementById('formGastos')) {
    const clienteSelect = document.getElementById('cliente');
    clienteSelect.addEventListener('change', event => {
      const clienteId = event.target.value;
      const reserva = reservas.find(r => r.hospedeId == clienteId);
      if (reserva) {
        document.getElementById('dias').value = reserva.dias;
      }
    });

    document.getElementById('frigobarSim').addEventListener('click', () => {
      frigobar = true;
    });

    document.getElementById('frigobarNao').addEventListener('click', () => {
      frigobar = false;
    });

    document.getElementById('formGastos').addEventListener('submit', event => {
      event.preventDefault();
      const clienteId = document.getElementById('cliente').value;
      const diarias = parseInt(document.getElementById('dias').value);
      const valorDiaria = 100;  // Exemplo de valor fixo para a diária
      const lavanderia = parseFloat(document.getElementById('lavanderia').value);
      const quarto = parseFloat(document.getElementById('quarto').value);

      calcularConta(clienteId, diarias, valorDiaria, frigobar, lavanderia, quarto);
    });

    hospedes.forEach(h => {
      const option = document.createElement('option');
      option.value = h.id;
      option.textContent = `${h.nome} (ID: ${h.id})`;
      clienteSelect.appendChild(option);
    });

    const btnCheckOut = document.getElementById('btnCheckOut');
    btnCheckOut.onclick = () => {
      const clienteId = document.getElementById('cliente').value;
      realizarCheckOut(clienteId);
    };
  }
});

function cadastrarHospede(dadosHospede) {
  dadosHospede.id = hospedes.length ? hospedes[hospedes.length - 1].id + 1 : 1;
  hospedes.push(dadosHospede);
  localStorage.setItem('hospedes', JSON.stringify(hospedes)); 
  atualizarDropdownHospedes(); // Atualiza a lista de hóspedes na reserva
}

function atualizarDropdownHospedes() {
  const hospedeSelect = document.getElementById('HospedeSelecionado');
  hospedeSelect.innerHTML = '';
  hospedes.forEach(h => {
    const option = document.createElement('option');
    option.value = h.id;
    option.textContent = `${h.nome} (ID: ${h.id})`;
    hospedeSelect.appendChild(option);
  });
}

function exibirHospedes() {
  const lista = document.getElementById('listaHospedes');
  lista.innerHTML = '';
  hospedes.forEach((h, index) => {
    const li = document.createElement('li');
    li.textContent = `ID: ${h.id}, Nome: ${h.nome}, CPF: ${h.cpf}`;

    const btnExcluir = document.createElement('button');
    btnExcluir.textContent = 'Excluir';
    btnExcluir.onclick = () => excluirHospede(index);

    li.appendChild(btnExcluir);
    lista.appendChild(li);
  });
}

function reservarQuarto(hospedeId, tipoQuarto, funcionarioId, precoQuarto, dias, quartoNumero) {
  const reserva = {
    id: reservas.length ? reservas[reservas.length - 1].id + 1 : 1,
    hospedeId,
    tipoQuarto,
    precoQuarto, 
    funcionarioId,
    quartoNumero,  // Novo campo para número do quarto
    checkin: false,
    dataReserva: new Date().toLocaleDateString(),
    dias
  };
  reservas.push(reserva);
  localStorage.setItem('reservas', JSON.stringify(reservas));
  alert(`Reserva realizada para o hóspede ${hospedeId} no quarto ${tipoQuarto} por R$${precoQuarto} por ${dias} dias.`);
  exibirReservas();
}

function realizarCheckIn(hospedeId) {
  const reserva = reservas.find(r => r.hospedeId === hospedeId && !r.checkin);
  if (reserva) {
    reserva.checkin = true;
    localStorage.setItem('reservas', JSON.stringify(reservas));
    alert('Check-in realizado com sucesso');
    listarClientesHospedados();
  } else {
    alert('Reserva não encontrada ou já em check-in');
  }
}

function realizarCheckOut(hospedeId) {
  const reserva = reservas.find(r => r.hospedeId === hospedeId && r.checkin);
  if (reserva) {
    reservas = reservas.filter(r => r.id !== reserva.id);
    localStorage.setItem('reservas', JSON.stringify(reservas));
    alert('Check-out realizado com sucesso');
    listarClientesHospedados();
  } else {
    alert('Nenhum check-in encontrado para esse hóspede');
  }
}

function excluirHospede(index) {
  if (confirm('Tem certeza que deseja excluir o hóspede ${hospedes[index].nome}?')) {
    hospedes.splice(index, 1);
    localStorage.setItem('hospedes', JSON.stringify(hospedes));
    exibirHospedes();
    alert('Hóspede excluído com sucesso');
  }
}

// Funções de Contabilidade
function calcularConta(hospedeId, diarias, valorDiaria, frigobar, lavanderia, quarto) {
  const totalFrigobar = frigobar ? 150 : 0;
  const total = (diarias * valorDiaria) + lavanderia + (quarto * diarias) + totalFrigobar;
  document.getElementById('totalGasto').textContent = `Total a pagar para o hóspede ${hospedeId}: R$${total.toFixed(2)}`;

  realizarCheckOut(hospedeId);  // Realiza o check-out após calcular a conta
}