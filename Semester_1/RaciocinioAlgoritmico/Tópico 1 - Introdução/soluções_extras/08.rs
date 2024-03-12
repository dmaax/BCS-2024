// Calcule a idade a partir do ano de nascimento (em anos, meses e dias)

fn main() {
  let ano_nascimento = 2000;
  let ano_atual = 2024;

  let idade_anos = ano_atual - ano_nascimento;
  let idade_meses = idade_anos * 12;
  let idade_dias = idade_anos * 365;

  println!("Idade em anos: {}, idade em meses: {}, idade em dias: {}", idade_anos, idade_meses, idade_dias)
}