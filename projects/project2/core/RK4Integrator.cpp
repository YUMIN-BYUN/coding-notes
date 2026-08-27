#include "RK4Integrator.h"

State RK4Integrator::step(
    const State& state,
    double time,
    double dt,
    const DerivativeFunction& derivative
) const
{
    State k1 = derivative(time, state);

    State temp(state.size());

    for (std::size_t i = 0; i < state.size(); ++i)
    {
        temp[i] = state[i] + 0.5 * dt * k1[i];
    }

    State k2 = derivative(time + 0.5 * dt, temp);

    for (std::size_t i = 0; i < state.size(); ++i)
    {
        temp[i] = state[i] + 0.5 * dt * k2[i];
    }

    State k3 = derivative(time + 0.5 * dt, temp);

    for (std::size_t i = 0; i < state.size(); ++i)
    {
        temp[i] = state[i] + dt * k3[i];
    }

    State k4 = derivative(time + dt, temp);

    State nextState(state.size());

    for (std::size_t i = 0; i < state.size(); ++i)
    {
        nextState[i]
            = state[i]
            + (dt / 6.0)
            * (k1[i] + 2.0 * k2[i]
                       + 2.0 * k3[i]
                       + k4[i]);
    }

    return nextState;
}