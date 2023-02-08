type matrice = int array array

let a = [| [|0;1;2|] |]
let b = [| [|0|]; [|1|]; [|2|] |]

exception Tailles_incompatibles

let somme_matriciel (a: matrice) (b : matrice) : matrice =
  let am = Array.length a in
  let an = Array.length a.(0) in
  let bm = Array.length b in
  let bn = Array.length b.(0) in
  if am <> bm || an <> bn then raise Tailles_incompatibles
  else
    let c = Array.make_matrix am an 0 in
    for i = 0 to am - 1 do
      for j = 0 to an - 1 do
        c.(i).(j) <- a.(i).(j) + b.(i).(j)
      done
    done;
    c


let produit_matriciel (a: matrice) (b : matrice) : matrice =
  let am = Array.length a in
  let an = Array.length a.(0) in
  let bm = Array.length b in
  let bn = Array.length b.(0) in
  if an <> bm then raise Tailles_incompatibles
  else
    let c = Array.make_matrix am bn 0 in
    for i = 0 to am - 1 do
      for j = 0 to bn - 1 do
        for k = 0 to an - 1 do
          c.(i).(j) <- c.(i).(j) + a.(i).(k) * b.(k).(j)
        done
      done
    done;
    c


(*let c = somme_matriciel a b*)
let d = produit_matriciel a b