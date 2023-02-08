type matrice = int array array

let A = [| [|1;2;3|]; [|4;5;6|]; [|7;8;9|] |]
let B = [| [|1;2;3|]; [|4;5;6|]; [|7;8;9|] |]

exception Tailles_incompatibles

let somme_matriciel (A: matrice) (B : matrice) : matrice =
  let am = Array.length A in
  let an = Array.length A.(0) in
  let bm = Array.length B in
  let bn = Array.length B.(0) in
  if am <> bm || an <> bn then raise Tailles_incompatibles
  else
    let C = Array.make_matrix am an 0 in
    for i = 0 to am - 1 do
      for j = 0 to an - 1 do
        C.(i).(j) <- A.(i).(j) + B.(i).(j)
      done
    done;
    C


let produit_matriciel (A: matrice) (B : matrice) : matrice =
  let am = Array.length A in
  let an = Array.length A.(0) in
  let bm = Array.length B in
  let bn = Array.length B.(0) in
  if an <> bm then raise Tailles_incompatibles
  else
    let C = Array.make_matrix am bn 0 in
    for i = 0 to am - 1 do
      for j = 0 to bn - 1 do
        for k = 0 to an - 1 do
          C.(i).(j) <- C.(i).(j) + A.(i).(k) * B.(k).(j)
        done
      done
    done;
    C


let C = somme_matriciel A B
let D = produit_matriciel A B