% rebase("_base.tpl")

<div class="container py-3">

    % if user.name is None:

        <form class="mx-auto" style="max-width: 24rem" method="POST">
            <p>Da začnete, vnesite svoje ime:</p>
            <div class="input-group">
                <input type="text" name="name" class="form-control" placeholder="Ime" aria-label="Ime" aria-describedby="button-addon">
                <div class="input-group-append">
                    <button class="btn btn-primary" type="submit" id="button-addon">Potrdi</button>
                </div>
            </div>
        </form>

    % else:

        <p>Dobrodošel, {{user.name}}!</p>

        % if len(games) > 0:
            <div class="d-flex justify-content-between mb-3">
                <h2 class="mr-3">Nadaljuj igro</h2>
                <form action="/igre" method="POST">
                    <a href="/igre" class="btn btn-light">
                        Vse igre
                    </a>
                    <button class="btn btn-primary" type="submit">
                        Nova igra
                    </button>
                </form>
            </div>
            <div class="row">
                % for game in games[:3]:
                    <div class="col-sm-12 col-md-4 px-md-1 pb-2">
                        <div class="card p-3">
                            % include("_matrix.tpl", game=game)
                            <div class="d-flex justify-content-between mt-3">
                                <span>{{game.state.progress()}} / 81</span>
                                <a href="/igre/{{game.id}}"
                                    class="btn btn-light">
                                    Nadaljuj
                                </a>
                            </div>
                        </div>
                    </div>
                % end
            </div>
        % else:
            <div class="d-flex justify-content-between">
                <h2 class="mr-3">Začni novo igro</h2>
                <form action="/igre" method="POST">
                    <button class="btn btn-primary" type="submit">
                        Nova igra
                    </button>
                </form>
            </div>
        % end
    % end

</div>