#include "EulerIntegrator.h"

State EulerIntegrator::step(
    const State& state,
    double time,
    double dt,
    const DerivativeFunction& derivative
) const
{
    State k1 = derivative(time, state);

    State nextState(state.size());

    for (std::size_t i = 0; i < state.size(); ++i)
    {
        nextState[i] = state[i] + dt * k1[i];
    }

    return nextState;
}