#ifndef EULER_INTEGRATOR_H
#define EULER_INTEGRATOR_H

#include "Integrator.h"

class EulerIntegrator : public Integrator
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