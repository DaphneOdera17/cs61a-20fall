(define (even? n)
  (zero? (remainder n 2)))

(define (sum-evens s)
  (if (null? s)
      0
      (if (even? (car s))
          (+ (car s) (sum-evens (cdr s)))
          (sum-evens (cdr s)))))