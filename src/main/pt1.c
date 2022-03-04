#include "pt1.h"

double y;
double u;

static double x;

static const double K = 1.0;
static const double T = 1.50;
static const double dt = 0.01;

void init(void)
{
    u = 0.0;
    y = 0.0;
    x = 0.0;
}

void step(void)
{
    x = y;
    y = x + (K * u - x) * dt / T;
}
