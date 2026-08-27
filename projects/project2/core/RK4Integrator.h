#ifndef RK4_INTEGRATOR_H
#define RK4_INTEGRATOR_H

#include "Integrator.h"

class RK4Integrator : public Integrator
{
public:
    State step(
        const State& state,
        double time,
        double dt,
        const DerivativeFunction& derivative
    ) const override;
};

#endif