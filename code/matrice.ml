type matrice = float array array

exception Tailles_incompatibles

let somme_matrice (a: matrice) (b : matrice) : matrice =
  let am = Array.length a in
  let an = Array.length a.(0) in
  let bm = Array.length b in
  let bn = Array.length b.(0) in
  if am <> bm || an <> bn then raise Tailles_incompatibles
  else
    let c = Array.make_matrix am an 0. in
    for i = 0 to am - 1 do
      for j = 0 to an - 1 do
        c.(i).(j) <- a.(i).(j) +. b.(i).(j)
      done
    done;
    c


let produit_matrice (a: matrice) (b : matrice) : matrice =
  let am = Array.length a in
  let an = Array.length a.(0) in
  let bm = Array.length b in
  let bn = Array.length b.(0) in
  if an <> bm then raise Tailles_incompatibles
  else
    let c = Array.make_matrix am bn 0. in
    for i = 0 to am - 1 do
      for j = 0 to bn - 1 do
        for k = 0 to an - 1 do
          c.(i).(j) <- c.(i).(j) +. a.(i).(k) *. b.(k).(j)
        done
      done
    done;
    c

let repr_matrice (a: matrice) : unit =
  let n = Array.length a in
  let m = Array.length a.(0) in
  for i = 0 to n - 1 do
    for j = 0 to m - 1 do
      Printf.printf "| %f |" a.(i).(j)
    done;
    Printf.printf "\n"
  done;
  Printf.printf "\n";
;;

let transposee_matrice (a: matrice) : matrice =
  let n = Array.length a in
  let m = Array.length a.(0) in
  let b = Array.make_matrix m n 0. in
  for i = 0 to n - 1 do
    for j = 0 to m - 1 do
      b.(j).(i) <- a.(i).(j)
    done
  done;
  b

let determinant_matrice (a: matrice) : float =
  let rec aux (a : matrice) : float =
    (*repr_matrice a;*)
    let det = ref 0. in
    let n = Array.length a in
    if n = 1 then a.(0).(0)
    else (
      let b = Array.make_matrix (n - 1) (n - 1) 0. in
      for k = 0 to n - 1 do
        (*Printf.printf "k = %d -> %d\n" k a.(k).(0);*)
        for i = 0 to n - 1 do
          for j = 1 to n - 1 do
            if i < k then b.(i).(j-1) <- a.(i).(j)
            else if i > k then b.(i-1).(j-1) <- a.(i).(j)
          done
        done;
        let sous_det = aux b in
        (*Printf.printf "sous_det %d = %d\n" k sous_det;*)
        if k mod 2 = 0 then det := !det +. a.(k).(0) *. sous_det
        else det := !det -. a.(k).(0) *. sous_det
      done;
      Printf.printf "det= %f\n" !det;
      !det
    )
  in
  let n = Array.length a in
  if n <> Array.length a.(0) then raise Tailles_incompatibles
  else aux a


let comatrice_matrice (a: matrice) : matrice =
  let n = Array.length a in
  let m = Array.length a.(0) in
  if n <> m then raise Tailles_incompatibles
  else
    let b = Array.make_matrix n m 0. in
    for i = 0 to n - 1 do
      for j = 0 to m - 1 do
        let c = Array.make_matrix (n - 1) (m - 1) 0. in
        for k = 0 to n - 1 do
          for l = 0 to m - 1 do
            if k < i && l < j then c.(k).(l) <- a.(k).(l)
            else if k < i && l > j then c.(k).(l-1) <- a.(k).(l)
            else if k > i && l < j then c.(k-1).(l) <- a.(k).(l)
            else if k > i && l > j then c.(k-1).(l-1) <- a.(k).(l)
          done;
        done;
        Printf.printf "comatrice %d %d\n" i j;
        b.(i).(j) <- (if (i+j) mod 2 = 0 then 1. else -1.) *. determinant_matrice c;
        Printf.printf "comatrice %d %d = %f\n" i j b.(i).(j);
      done;
    done;
    b
;;

let produit_lambda_matrice (lambda : float) (a : matrice) : matrice =
  let n = Array.length a in
  let m = Array.length a.(0) in
  for i = 0 to n-1 do
    for j = 0 to m-1 do
      a.(i).(j) <- lambda *. a.(i).(j)
    done;
  done;
  a

let inverse_matrice (a : matrice) : matrice =
  let n = Array.length a in
  let m = Array.length a.(0) in
  if n <> m then raise Tailles_incompatibles
  else (
    produit_lambda_matrice (1. /. determinant_matrice a) (transposee_matrice (comatrice_matrice a))
  )
    
let m = [| [| 5.; 7.; -3. |]; [| 4.; 2.; -1. |]; [| 9.; -4.; 6. |] |];;

1. /. (determinant_matrice m);;
repr_matrice (transposee_matrice (comatrice_matrice m));;
(* produit_lambda_matrice 2. m;; *)
repr_matrice (inverse_matrice m);;
