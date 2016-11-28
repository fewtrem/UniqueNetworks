C
      SUBROUTINE SIMULATE(W,VR,I_c,VT,TAU_MD,N,V,VI,DT,EN)
C
      ! Weights in matrix:
      REAL :: W(*)
      ! Reset Voltage
      REAL :: VR(*)
      ! Input Current
      REAL :: I_c(*)
      ! Threshold Voltage
      REAL :: VT(*)
      ! Time constant]
      REAL :: TAU_MD(*)
      ! Get size of input:
      INTEGER :: N
      ! actual V
      REAL ::  V(*)
      ! endtime
      REAL :: EN
      REAL :: T
      T = 0.0
      DO 20 J = 1, N
         V(J) = VI(J)
20    CONTINUE
      DO 22 WHILE (T .LT. EN)
      DO 21 J = 1, N
         V(J) = V(J)-(V(J)-I_c(J))*TAU_MD(J)*DT
21    CONTINUE
      T = T+DT
22    CONTINUE
      END
