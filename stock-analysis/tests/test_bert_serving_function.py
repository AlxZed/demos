from functions.bert_serving_function import SentimentClassifierServing
import mlrun

event_data = {'inputs': ['By Herbert Lash', 'NEW YORK (Reuters) - The blue-chip Dow powered to its fifth '
                                               'consecutive record high on Friday and the S&P 500 closed slightly '
                                               'higher as investors bought shares that should benefit from a strong '
                                               'reopening of the U.S. economy, an outlook signaled by rising yields '
                                               'in the bond market.', 'The tech-heavy Nasdaq tumbled after rebounding '
                                                                      'more than 6% over the past three sessions as '
                                                                      'the rising bond yields revived inflation '
                                                                      'worries and dulled the appeal of high-growth '
                                                                      'technology shares.', 'The S&P 500 and Nasdaq '
                                                                                            'posted their biggest '
                                                                                            'weekly percentage gains '
                                                                                            'since early February '
                                                                                            'after President Joe '
                                                                                            'Biden signed into law on '
                                                                                            'Thursday one of the '
                                                                                            'largest U.S. fiscal '
                                                                                            'stimulus bills and data '
                                                                                            'reinforced convictions '
                                                                                            'the economy was headed '
                                                                                            'to a high-growth '
                                                                                            'recovery.', 'The recent '
                                                                                                         'rise in '
                                                                                                         'U.S. '
                                                                                                         'Treasury '
                                                                                                         'yields has '
                                                                                                         'raised '
                                                                                                         'fears of a '
                                                                                                         'sudden '
                                                                                                         'tapering of '
                                                                                                         'monetary '
                                                                                                         'stimulus '
                                                                                                         'and put '
                                                                                                         'downward '
                                                                                                         'pressure on '
                                                                                                         'Wall Street '
                                                                                                         'in recent '
                                                                                                         'weeks.',
                            'The yield on the benchmark 10-year note hit 1.642% on Friday, the highest level since '
                            'February of last year. [US/]', 'Boeing  Co rose 6.82% to lead the Dow and S&P 500 '
                                                            'higher. The rising Dow and tumbling Nasdaq reflect an '
                                                            'ongoing sell-off in tech as investors buy cyclical and '
                                                            'underpriced value stocks that are expected to do well as '
                                                            'the economy recovers.', 'For tech stocks to continue to '
                                                                                     'flourish you need low rates, '
                                                                                     'and in effect slower growth, '
                                                                                     'said Thomas Hayes, chairman and '
                                                                                     'managing member of hedge fund '
                                                                                     'Great Hill Capital LLC. ',
                            'But with the stimulus package the economy is likely to expand 7% to 9% this year and '
                            'pressure interest rates, he said.', '"That s why you re seeing rates rise today because '
                                                                 'the reopening is happening faster and stronger than '
                                                                 'anticipated. And that s when value and cyclicals '
                                                                 'and economically sensitive stocks outperform,'
                                                                 '" Hayes said.', 'The speedy distribution of '
                                                                                  'vaccines and more fiscal aid have '
                                                                                  'spurred concerns of rising '
                                                                                  'inflation despite assurances from '
                                                                                  'the Federal Reserve to maintain an '
                                                                                  'accommodative policy. All eyes '
                                                                                  'will be on the central bank s '
                                                                                  'policy meeting next week for '
                                                                                  'further cues on inflation.',
                            'U.S. consumer sentiment improved in early March to its strongest in a year, a survey by '
                            'the University of Michigan showed on Friday.', 'The Dow Jones Industrial Average rose '
                                                                            '293.05 points, or 0.9%, to close at 32,'
                                                                            '778.64 and the S&P 500 gained 4 points, '
                                                                            'or 0.10%, to 3,943.34. The Nasdaq '
                                                                            'Composite dropped 78.81 points, '
                                                                            'or 0.59%, to end at 13,319.87.',
                            'For the week, the S&P rose 2.6%, the Dow added 4.1% and the Nasdaq gained 3.1%. For the '
                            'Dow it was its biggest weekly gain since November.', 'Volume on U.S. exchanges was 11.64 '
                                                                                  'billion shares.', 'The Nasdaq has '
                                                                                                     'been '
                                                                                                     'particularly '
                                                                                                     'hit by the '
                                                                                                     'sell-off in '
                                                                                                     'recent weeks '
                                                                                                     'and confirmed a '
                                                                                                     'correction at '
                                                                                                     'the start of '
                                                                                                     'the week as '
                                                                                                     'investors '
                                                                                                     'swapped richly '
                                                                                                     'valued '
                                                                                                     'technology '
                                                                                                     'stocks with '
                                                                                                     'those of '
                                                                                                     'energy, '
                                                                                                     'mining and '
                                                                                                     'industrial '
                                                                                                     'companies that '
                                                                                                     'are poised to '
                                                                                                     'benefit more '
                                                                                                     'from an '
                                                                                                     'economic '
                                                                                                     'rebound.',
                            'Value stocks added about 0.80%, while growth stocks slumped 0.62% in a continuation of a '
                            'rotation that began late last year.', 'The high-flying but yield-sensitive group of '
                                                                   'stocks including of  Facebook Inc  , Apple Inc , '
                                                                   'Amazon.com Inc , Netflix Inc , Google-parent '
                                                                   'Alphabet  Inc, Tesla  Inc and  Microsoft Corp  , '
                                                                   'which fueled the past s year rally, fell.',
                            'Tech, communication services and consumer discretionary indexes, which house these '
                            'mega-cap stocks, slipped the most among major S&P sectors.', 'The bank index jumped '
                                                                                          '1.83%, while financials '
                                                                                          'and industrials clinched '
                                                                                          'new record levels.',
                            'Ulta Beauty  Inc fell 8.4% after the cosmetics retailer forecast annual revenue below '
                            'estimates, as demand for make-up products were under pressure due to extended '
                            'work-from-home policies.', 'U.S.-listed shares of China-based JD .com Inc slid 6.7% '
                                                        'after three sources said the company is in talks to buy part '
                                                        'or all of a stake in brokerage Sinolink Securities worth at '
                                                        'least $1.5 billion.', 'Advancing issues outnumbered '
                                                                               'declining ones on the NYSE by a '
                                                                               '1.24-to-1 ratio; on Nasdaq, '
                                                                               'a 1.14-to-1 ratio favored '
                                                                               'advancers.', '', 'The S&P 500 posted '
                                                                                                 '83 new 52-week '
                                                                                                 'highs and no new '
                                                                                                 'lows; the Nasdaq '
                                                                                                 'Composite recorded '
                                                                                                 '396 new highs and '
                                                                                                 '12 new lows. ']}


def test_serving_function():
    models_path = 'models/'
    fn = mlrun.new_function('my_server', kind='serving')
    # set the topology/router and add models
    graph = fn.set_topology("router")
    fn.add_model("model1", class_name='SentimentClassifierServing', model_path=models_path)
    #fn.add_model("model2", class_name="ClassifierModel", model_path="<path2>")
    # create and use the graph simulator
    server = fn.to_mock_server()
    result = server.test("/v2/models/model1/infer", event_data)




