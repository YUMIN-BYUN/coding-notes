#ifndef INTEGRATOR_H
#define INTEGRATOR_H

#include "State.h"
#include <functional>

using DerivativeFunction =
    std::function<State(double, const State&)>;

class Integrator
{
public:
    virtual ~Integrator() = default;

    virtual State step(
        const State& state,
        double time,
        double dt,
        const DerivativeFunction& derivative
    ) const = 0;
};

#endif