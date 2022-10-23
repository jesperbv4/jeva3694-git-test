#include <iostream>
using namespace std;

int main()
{
    int startnmr, vinnare, h, h_ny, h0, h1, m, m_ny, m0, m1, s, s_ny, s0, s1;
    int deltagare = 0;
    bool ny_ledare = false;

    // Läs in startnummer
    do
    {
        cout << "Startnummer? ";
        cin >> startnmr;
        // Om startnummret är större än 0
        if(startnmr > 0)
        {
            //Läs in start och måltid och öka antalet deltagare
            cout << "Starttid? ";
            cin >> h0 >> m0 >> s0;
            cout << "Måltid? ";
            cin >> h1 >> m1 >> s1;
            deltagare++;

            //Räkna ut tiden mellan start och mål
            h_ny = h1 - h0;
            m_ny = m1 - m0;
            s_ny = s1 - s0;

            //Tidsformatering
            if(s_ny < 0)
            {
                s_ny = s_ny + 60;
                m_ny = m_ny-1;
            }

            if(m_ny < 0)
            {
                m_ny = m_ny + 60;
                h_ny = h_ny-1;
            }

            if(h_ny < 0)
            {
                h_ny = h_ny + 24;
            }


            //Spara startnummer och tid för första deltagaren
            if(deltagare == 1)
            {
                vinnare = startnmr;
                h = h_ny;
                m = m_ny;
                s = s_ny;
            }

            //Jämför en ny deltagares tid med den bästa sparade tiden
            if(deltagare > 1)
            {
                if(h > h_ny)
                {
                    ny_ledare = true;
                }

                else if(h == h_ny)
                {

                    if(m > m_ny)
                    {
                      ny_ledare = true;
                    }

                    else if(m == m_ny)
                    {

                        if(s > s_ny)
                        {
                            ny_ledare = true;
                        }

                    }
                }
                // Om tiden är bättre, spara starnummer och tid
                if(ny_ledare == true)
                {
                    h = h_ny;
                    m = m_ny;
                    s = s_ny;
                    vinnare = startnmr;
                    ny_ledare = false;
                }

            }


        }
    // Bryter om startnummer är mindre än 1 anges
    } while(startnmr > 0);

    // Utskrift om det finns deltagare
    if(deltagare > 0)
    {
        cout << "Vinnare är starnr: " << vinnare << endl;
        cout << "Tim: " << h << " Min: " << m << " Sek: " << s << endl;
        cout << "Antal tävlande: " << deltagare << endl;
        cout << "Programmet avslutas" << endl;
    }
    // Utskrift om deltagare saknas
    else
    {
        cout << "Inga tävlande"<< endl;
        cout << "Programmet avslutas" << endl;
    }

    return 0;


}